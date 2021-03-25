from django.contrib import admin
from django.urls import path
from products_shop4u import views
urlpatterns = [
    path('',views.ok),
]