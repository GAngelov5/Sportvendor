
from django.conf.urls import url
from django.contrib.auth.views import *
from items import views

urlpatterns = [
    url(r'^$', views.search_for_item, name="search_view"),
    url(r'^(?P<item_pk>\d+)/$', views.view_item, name="item_view"),
    url(r'^delete/(?P<item_pk>\d+)/$', views.delete_item, name="delete_item"),
    url(r'^(?P<item_pk>\d+)/add_to_cart/$',
        views.add_to_cart,
        name="add_to_basket")
]
