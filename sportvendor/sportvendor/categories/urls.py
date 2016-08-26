
from django.conf.urls import url
from django.contrib.auth.views import *
from categories import views

urlpatterns = [
    url(r'^$', views.view_categories, name="view_categories"),
    url(r'^(?P<category_pk>\d+)/',
        views.view_category_items,
        name="category_items"),
]
