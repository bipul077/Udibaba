from django.shortcuts import render
from .models import Banner

# Create your views here.
def home(request):
    banners = Banner.objects.all().order_by('-id')
    return render(request,'index.html',{'banner':banners})

def cart(request):
    return render(request, 'cart/cart.html')

def contact(request):
    return render(request, 'contact/contact.html')

def about(request):
    return render(request, 'aboutus/about.html')

def review(request):
    return render(request, 'review/review.html')

def menu(request):
    return render(request, 'menu/menu.html')