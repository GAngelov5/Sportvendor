from django.shortcuts import render
from .models import Item
from basket.models import Basket
from categories.models import Category
from brand.models import Brand
from basket.views import view_basket
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def view_item(request, item_pk):
    item = Item.objects.get_item(item_pk)
    return render(request,
                  "items/item.html",
                  {"name": item.name,
                   "quality": item.quality,
                   "added_on": item.added_on,
                   "info": item.made_from,
                   "size": item.size,
                   "price": item.price,
                   "item_id": item.id,
                   "img_url": item.image})


@login_required
def delete_item(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    item.delete()
    return view_basket(request)


@login_required
def add_to_cart(request, item_pk):
    item = Item.objects.get_item(item_pk)
    basket = Basket.objects.get(user=request.user)
    basket.basket_items.add(item)
    return render(request,
                  "items/item.html",
                  {"name": item.name,
                   "quality": item.quality,
                   "added_on": item.added_on,
                   "info": item.made_from,
                   "size": item.size,
                   "price": item.price,
                   "item_id": item.id})


@login_required(login_url='login')
def search_for_item(request):
    search_by = request.GET.get("selected_option").lower()
    #  print(request.GET.get("search_input"))
    items = Item.objects.none()
    if search_by == "name":
        items = Item.objects.filter(name=request.GET.get("search_input"))
    elif search_by == "category":
        category = Category.objects.none()
        try:
            category = Category.objects.get(name=request.GET.get("search_input"))
        except Category.DoesNotExist:
            print("Fail category search")
        if category:
            items = Item.objects.filter(category=category.id)
    elif search_by == "brand":
        brand = Brand.objects.none()
        try:
            brand = Brand.objects.get(name=request.GET.get("search_input"))
        except Brand.DoesNotExist:
            print('Fail brand search')
        if brand:
            items = Item.objects.filter(brand=brand.id)
    else:
        items = Item.objects.filter(price__gt=request.GET.get("search_input"))
    return render(request,
                  "items/search_items.html",
                  {"searching_results": items.all()})
