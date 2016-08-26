from django.shortcuts import render
from .models import Basket
from discount.models import Discount
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.mail import send_mail
from .forms import CreditCardForm
from billing.utils.credit_card import CreditCard
from billing.gateway import get_gateway
import string
import random
import decimal
# Create your views here.


@login_required(login_url='login')
def view_basket(request):
    try:
        basket = Basket.objects.get(user=request.user)
    except Basket.DoesNotExist:
        basket = Basket.objects.create_basket(request.user)
    basket = Basket.objects.get(user=request.user)
    total_price = get_total_price(basket, request)
    return render(request,
                  "basket/basket.html",
                  {"name": basket.name,
                   "created_on": basket.create_date,
                   "basket_items": basket.basket_items.all(),
                   "total": total_price})


@login_required
def confirm_basket(request):
    return render_confirmation_page(request, "", False)


@login_required
def send_confirmation(request):
    random_chars = [random.choice(string.ascii_letters +
                                  string.digits) for n in range(30)]
    confirmation_code = "".join(random_chars)
    if 'code' not in request.session:
        request.session['code'] = confirmation_code

    if request.GET.get("confirmation_input") is None:
        send_mail("Hello",
                  "Confirmation code: " + request.session['code'],
                  "galin.angelov5@yahoo.com",
                  ["galin.angelov5@gmail.com"],
                  fail_silently=False)
        return confirm_basket(request)
    else:
        if request.GET.get("confirmation_input") == request.session['code']:
            return render_confirmation_page(request,
                                            "Successful confirmation!",
                                            True)
        #  in order mail doesn't/ usually it works but
        #  some problems with the new yahoo account
        elif request.GET.get("confirmation_input") == "12345":
            return render_confirmation_page(request,
                                            "Successful confirmation!",
                                            True)
        else:
            return render_confirmation_page(request,
                                            "Wrong code. Try Again!",
                                            False)


@login_required
def render_confirmation_page(request, confirmation_msg, success):
    basket = Basket.objects.get(user=request.user)
    total_price = get_total_price(basket, request)
    item_count = len(basket.basket_items.all())
    give_discount = total_price > 100
    total = float(decimal.Decimal(total_price))
    discount = None
    if give_discount:
        discount = generate_discount(request)
        total = total - total * (discount.discount / float(100))
        total_price = total
        current_user = request.user.customer
        if discount not in current_user.discounts.all():
            current_user.discounts.add(discount)
    if discount:
        discount = discount.name
    return render(request,
                  "basket/confirmation.html",
                  {"item_count": item_count,
                   "total": total_price,
                   "give_discount": give_discount,
                   "discount": discount,
                   "confirmation_msg": confirmation_msg,
                   "confirmation_successful": success})


@login_required
def payment_provider(request):
    form = CreditCardForm()
    return render(request,
                  "basket/payment_provider.html",
                  {"form": form})


@login_required
def process_credit_card(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            paypal_provider = get_gateway("pay_pal")
            cc = CreditCard(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            month=form.cleaned_data['month'],
                            year=form.cleaned_data['year'],
                            number=form.cleaned_data['number'],
                            verification_value=form.cleaned_data['verify_val'])
            basket = Basket.objects.get(user=request.user)
            total_price = get_total_price(basket, request)
            paypal_provider.purchase(total_price,
                                     cc,
                                     options={"request": request})
            #  PayPalFailure('Security header is not valid')
            current_user = request.user.customer
            for item in basket.basket_items.all():
                current_user.items_history.add(item)
            basket.basket_items.clear()
            current_user.discounts.clear()
    return render(request,
                  "basket/payment_done.html",
                  {"success": "Successfully purchased!"})


def generate_discount(request):
    basket_items = Basket.objects.get(user=request.user).basket_items.all()
    item = random.choice(basket_items)

    category = random.choice(item.category_set.all())
    discounts = Discount.objects.all()
    discount = random.choice(discounts)
    for current_discount in discounts:
        if current_discount.name == category.name:
            discount = current_discount

    return discount


def get_total_price(basket, request):
    total = basket.basket_items.all().aggregate(Sum('price'))
    return total['price__sum']
