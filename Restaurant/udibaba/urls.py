from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.home,name="home"),
     path('cart/', views.cart, name='cart'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('review/', views.review, name='review'),
     path('menu/', views.menu, name='menu'),
]