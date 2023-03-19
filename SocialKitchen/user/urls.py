from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from user import views as user_views

urlpatterns= [
    path("register", user_views.index, name="register_account"),
    path("admin/", admin.site.urls)
]