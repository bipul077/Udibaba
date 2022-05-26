from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

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