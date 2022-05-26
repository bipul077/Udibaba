from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def cart(request):
    return render(request, 'cart/cart.html')