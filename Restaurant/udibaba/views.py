from django.shortcuts import render
from django.contrib import messages
from .models import Banner, Gallery, Video, Product, Category,Event,Contact
from django.shortcuts import render,get_object_or_404,redirect
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
    request.method == "POST"   
    if request.method == "POST":
        ename = request.POST.get('name') 
        email = request.POST.get('email')
        msge = request.POST.get('message')
        print(ename,email,msge)
        contact = Contact(uname=ename,email=email,message=msge)
        contact.save()
        messages.success(request,'Message sent succesfully')
        return redirect('/contact')
    return render(request,'contact/contact.html')

def about(request):
    return render(request, 'aboutus/about.html')

def review(request):
    return render(request, 'review/review.html')

def menu(request):
    menu = Category.objects.all()
    return render(request, 'menu/menu.html',{'menu':menu})

def menulist(request,pk):
    menulists = Product.objects.filter(category=pk)
    print(menulists)
    return render(request, 'menu/menulist.html',{'menulists':menulists})

def gallery(request):
    gal =  Gallery.objects.all()
    context = {
        'gallery_list':gal,
    }
    return render(request, 'gallery/gallery.html', context)