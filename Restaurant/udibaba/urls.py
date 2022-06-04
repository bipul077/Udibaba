from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
     path('', views.home,name="home"),
     path('cart/', views.cart, name='cart'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('review/', views.review, name='review'),
     path('menu/', views.menu, name='menu'),
     path('gallery/', views.gallery, name='gallery'),
     path('signup/', views.signup, name='signup'),
     path('login/', LoginView.as_view(template_name = 'user/login.html'), name='login'),
     path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout')
]