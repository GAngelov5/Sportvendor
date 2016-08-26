from django.shortcuts import render
from .forms import UserProfile, UserRegister
from items.models import Item
import random
from basket.models import Basket
from users.models import Customer
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    all_items = Item.objects.all()
    few_items = []
    for i in range(0, 3):
        random_item = random.choice(all_items)
        if random_item not in few_items:
            few_items.append(random_item)
    return render(request,
                  "users/home.html",
                  {"title": "SportVendor",
                   "items": few_items,
                   "user": request.user})


def login_view(request):
    user = authenticate(username=request.POST.get("username"),
                        password=request.POST.get('password'))
    if user is not None:
        login(request, user)

        return HttpResponseRedirect('/')
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_view(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            new_user = form.save()
            Customer.objects.create(user=new_user)
            Basket.objects.create_basket(new_user)
            return HttpResponseRedirect('/user/login')
    else:
        form = UserRegister()
    return render(request, "register.html", {'form': form})


@login_required(login_url='login')
def profile_view(request):
    if request.method == 'POST':
        form = UserProfile(request.POST, instance=request.user)
        if form.is_valid():
            update_user = Customer.objects.get(id=request.user.id)
            update_user.first_name = form.cleaned_data['first_name']
            update_user.last_name = form.cleaned_data['last_name']
            update_user.save()
            return HttpResponseRedirect('/')
    else:
        form = UserProfile(instance=request.user)
    return render(request, "profile.html", {'form': form})


@login_required
def update_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {'form': form})


@login_required
def get_user_history(request):
    items = []
    try:
        current_user = request.user.customer
        items = current_user.items_history.all()
    except ObjectDoesNotExist:
        print("Catch fail")
    return render(request,
                  "show_user_history.html",
                  {"items": items})
