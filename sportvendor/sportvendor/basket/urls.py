from django.conf.urls import url
from django.contrib.auth.views import *
from basket import views

urlpatterns = [
    url(r'^$', views.view_basket, name="basket_view"),
    url(r'^confirmation/', views.confirm_basket, name="proceed_basket"),
    url(r'^send_confirmation/',
        views.send_confirmation,
        name="send_confirmation"),
    url(r'^submit_provider/', views.payment_provider, name="payment_provider"),
    url(r'^process_providing/',
        views.process_credit_card,
        name="process_provider"),
    url(r'^generate_discount/',
        views.generate_discount,
        name='discount_ticket')
]
