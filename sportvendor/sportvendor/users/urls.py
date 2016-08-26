from django.conf.urls import url
from django.contrib.auth.views import *
from users import views

urlpatterns = [
    url(r'^login$', views.login_view, name="login"),
    url(r'^logout$', views.logout_view, name="logout"),
    url(r'^register$', views.register_view, name="register"),
    url(r'^profile$', views.profile_view, name="profile"),
    url(r'^change-password$', views.update_view, name="change_pass"),
    url(r'^user_item_history$', views.get_user_history, name="item_history")
]
