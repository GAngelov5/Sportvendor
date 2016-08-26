from django.conf.urls import url
from django.contrib.auth.views import *
from brand import views

urlpatterns = [
    url(r'^$', views.view_brands, name="view_brands"),
    url(r'^(?P<brand_pk>\d+)/',
        views.view_brand_items,
        name="brand_items")
]
