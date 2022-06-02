from django.shortcuts import render
from .models import Banner, Gallery, Video, Product, Category,Event
# Create your views here.
def home(request):
    banners = Banner.objects.all().order_by('-id')
    video = Video.objects.all()
    featured = Product.objects.filter(is_featured=True)
    abc = Event.objects.count()
    if abc:
        event = Event.objects.get()
        context = {'banner':banners,
        'video':video,
        'featured':featured,
        'event':event,
        }
    else:
        context = {'banner':banners,
        'video':video,
        'featured':featured,
        }
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
    menu = Category.objects.all()
    return render(request, 'menu/menu.html',{'menu':menu})

def gallery(request):
    gal =  Gallery.objects.all()
    context = {
        'gallery_list':gal,
    }
    return render(request, 'gallery/gallery.html', context)