from django.shortcuts import render
from brand.models import Brand
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def view_brands(request):
    brands = Brand.objects.all()
    return render(request,
                  "brand/brands.html",
                  {"brands": brands})


@login_required
def view_brand_items(request, brand_pk):
    brand = Brand.objects.get(id=brand_pk)
    items = brand.item_set.all()
    return render(request,
                  "brand/brand_items.html",
                  {"items": items})
