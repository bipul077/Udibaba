from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
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
    if request.method == 'POST':
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

def profile(request):
    return render(request, 'profile/profile.html')

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

#Customer Registration
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('fullname').split(' ')
            
            usr = User.objects.get(username=username)
            usr.email = email
            usr.first_name = name[0]
            usr.last_name = name[1]
            usr.save()
            messages.success(request, f'Congratulations!! Account created for {username}')
            return redirect('login')
    else:
        form = SignUpForm()
        
    return render(request, 'user/signup.html', {'form':form})
    