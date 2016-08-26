from django.shortcuts import render
from categories.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def view_categories(request):
    categories = Category.objects.all()
    return render(request,
                  "categories/category.html",
                  {"categories": categories})


@login_required
def view_category_items(request, category_pk):
    items = Category.objects.get_category_items(category_pk)
    return render(request,
                  "categories/category_items.html",
                  {"items": items})
