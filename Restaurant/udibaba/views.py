from django.shortcuts import render, redirect
from .forms import SignUpForm, ReviewForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Banner, Gallery, Video, Product, Category, Event, Contact, Cart, UserOTP, Review
from django.http.response import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
import random
from django.core.mail import send_mail #for otp
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login #inbuilt function
from django.contrib.auth.decorators import login_required #for function based view

def home(request):
    banners = Banner.objects.all().order_by('-id')
    video = Video.objects.all()
    featured = Product.objects.filter(is_featured=True)
    myreviews = Review.objects.filter(status=True)
    if request.user.is_authenticated:
        abc = Event.objects.count()
        if abc:
            event = Event.objects.get()
            context = {'banner':banners,
            'video':video,
            'featured':featured,
            'event':event,
            'review':myreviews,
            }
        else:
            context = {'banner':banners,
            'video':video,
            'featured':featured,
            'review':myreviews,
            }
        return render(request,'home.html',context)

def cart(request):
    return render(request, 'cart/cart.html')

def addtocart(request):
    print("yahoo")
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                return JsonResponse({'status':"Product Already in Cart"})
            else:
                prod_qty = int(request.POST.get('product_qty'))   
                Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                cart = Cart.objects.filter(user=request.user)
                cartcount = cart.count()
                context = {
                    'cartcount':cartcount,
                    'status':"Product Added Successfully"
                }
                return JsonResponse(context)     
        else:
            return JsonResponse({'status':"Login to Continue"})

def contact(request):
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
    if request.method == "POST":
        get_otp = request.POST.get('otp') #comes for signup.html "name"
        
        #To handle undefined otp
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr) 
            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                messages.success(request, f'Congratulations!! Account created for {usr.username}')
                return redirect('login')
            else:
                messages.warning(request, f'You Entered a wrong OTP.')
                return render(request, 'user/signup.html', {'otp':True, 'usr':usr}) #To take otp

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')
            usr = User.objects.get(username=username)
            usr.email = username
            usr.first_name = name[0]
            usr.last_name = name[1]
            usr.is_active = False
            usr.save()
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user = usr, otp = usr_otp)
            print("hi" + str(usr_otp))
            
            mess = f"Hello {usr.first_name}, \nYour OTP is {usr_otp}\nThanks!"
            
            send_mail(
                "Welcome to Udibaba - Verify Your Email Address", #1 argument - subject
                mess, #2 argument - message
                settings.EMAIL_HOST_USER, #3 argument - host user
                [usr.email], #4 argument - whom to send
                fail_silently = False # 5 argument - fail silently
            )
            
        return render(request, 'user/signup.html', {'otp':True, 'usr':usr}) #To take otp
    else:
        form = SignUpForm()
        
    return render(request, 'user/signup.html', {'form':form})

#resend otp
def resend_otp(request):
    if request.method == "GET":
        get_usr = request.GET['usr']
        if User.objects.filter(username = get_usr).exists() and not User.objects.get(username = get_usr).is_active:
            usr = User.objects.get(username = get_usr)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user = usr, otp = usr_otp)
            
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"
            send_mail(
                "Welcome to Udibaba - Verify Your Email Address", #1 argument - subject
                mess, #2 argument - message
                settings.EMAIL_HOST_USER, #3 argument - host user
                [usr.email], #4 argument - whom to send
                fail_silently = False # 5 argument - fail silently
            )
            return HttpResponse("Resend")
    return HttpResponse("Cannot Send ") 

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        get_otp = request.POST.get('otp') #comes for signup.html "name"
        
        #To handle undefined otp
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr) 
            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                login(request, usr)
                return redirect('home')
            else:
                messages.warning(request, f'You Entered a wrong OTP.')
                return render(request, 'user/login.html', {'otp':True, 'usr':usr}) #To take otp
        
        usrname = request.POST['username']    
        pword = request.POST['password']
        
        user = authenticate(request, username = usrname, password = pword) #it returns none when username and password is invalid
        if user is not None:
            login(request, user)
            return redirect('home')
        elif not User.objects.filter(username = usrname).exists():
            messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
        elif not User.objects.get(username = usrname).is_active:
            usr = User.objects.get(username = usrname)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user = usr, otp = usr_otp)
            
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"
            send_mail(
                "Welcome to Udibaba - Verify Your Email Address", #1 argument - subject
                mess, #2 argument - message
                settings.EMAIL_HOST_USER, #3 argument - host user
                [usr.email], #4 argument - whom to send
                fail_silently = False # 5 argument - fail silently
            )
            return render(request, 'user/login.html', {'otp':True, 'usr':usr}) #To take otp
        else:
            messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')

    form = AuthenticationForm()   
    return render(request, 'user/login.html', {'form':form})

def submit_review(request):
    if request.user.is_authenticated:
        url = request.META.get('HTTP_REFERER')
        if request.method == "POST":
            try:
                reviews = Review.objects.get(user__id=request.user.id)
                form = ReviewForm(request.POST, instance=reviews)
                form.save()
                messages.success(request, 'Your reviews has been updated!!')
                return redirect(url)
            except Review.DoesNotExist:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    data = Review()
                    data.subject = form.cleaned_data['subject']
                    data.review = form.cleaned_data['review']
                    data.rating = form.cleaned_data['rating']
                    data.ip = request.META.get('REMOTE_ADDR')
                    data.user_id = request.user.id
                    data.save()
                    messages.success(request, 'Thank you! Your review has been submitted')
                    return redirect(url)
                return render(request, 'review/review.html')
    messages.error(request, 'You must be login to provide a review.')
    return redirect('review')
                


                
            

    
            
        
    