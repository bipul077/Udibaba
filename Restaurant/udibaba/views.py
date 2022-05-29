from django.shortcuts import render
from .models import Banner, Gallery, Video, Product, Category, Event
# Create your views here.
def home(request):
    banners = Banner.objects.all().order_by('-id')
    video = Video.objects.all()
    events = Event.objects.get()
    featured = Product.objects.filter(is_featured=True)
    context = {'banner':banners,'video':video,'event':events,'featured':featured}
    return render(request,'home.html',context)

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

def gallery(request):
    gal =  Gallery.objects.all()
    context = {
        'gallery_list':gal,
    }
    return render(request, 'gallery/gallery.html', context)
