

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.fun1,name='login'),
    path('fblogin',views.fun2,name='fblogin'),
    path('javascript',views.fun3,name='javascript')
]