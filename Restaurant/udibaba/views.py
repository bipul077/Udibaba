from django.shortcuts import render
<<<<<<< HEAD
from .models import Banner,Video,Product
=======
from .models import Banner
>>>>>>> origin/rijanbranch

# Create your views here.
def home(request):
    banners = Banner.objects.all().order_by('-id')
<<<<<<< HEAD
    video = Video.objects.all()
    featured = Product.objects.filter(is_featured=True)
    context={'banner':banners,'video':video,'featured':featured}
    return render(request,'home.html',context)
=======
    return render(request,'index.html',{'banner':banners})
>>>>>>> origin/rijanbranch

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