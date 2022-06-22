from zipapp import create_archive
from django.shortcuts import render, redirect
from .forms import SignUpForm, ReviewForm, CustomerAddressForm, CustomerDetailsUpdateForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from .models import Banner, Gallery, Video, Product, Category, Event, Contact, Review, UserOTP, Order, OrderItem, CustomerProfile
from django.http.response import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
import random
from django.core.mail import send_mail #for otp
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login #inbuilt function
from django.contrib.auth.decorators import login_required #for function based view
from django.utils.decorators import method_decorator #for class based view
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django_mail_admin import mail

def home(request):
    banners = Banner.objects.all().order_by()
    video = Video.objects.all()
    featured = Product.objects.filter(is_featured=True)
    myreviews = Review.objects.filter(status=True)
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
    menu = Category.objects.all().order_by('id')[:4]
    totaldata = Category.objects.all().count()
    return render(request, 'menu/menu.html',{'menu':menu,'totaldata':totaldata})

#update Customer Details
@login_required
def profile(request):
    if request.method == "POST":
        u_form = CustomerDetailsUpdateForm(request.POST, instance = request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error updating your profile')
    else:
        u_form = CustomerDetailsUpdateForm(instance=request.user)
            
    context = {
        'u_form':u_form,
        'activea':'btn-success',
    }

    return render(request, 'profile/profile.html', context)

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
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            # name = form.cleaned_data.get('name').split(' ')
            usr = User.objects.get(username=username)
            usr.email = username
            usr.first_name = firstname
            usr.last_name = lastname
            # usr.first_name = name[0]
            # usr.last_name = name[1]
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
            mess = f"Welcome {user.first_name} {user.last_name}"
            messages.success(request, mess)
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

#review
@login_required
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

# Cart List Page
def cart_list(request):
	total_amt=0  
	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['quan'])*float(item['price'])
		return render(request, 'cart/cart.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'totalamount':total_amt,'finalamount':total_amt+70})
	else:
		return render(request, 'cart/cart.html',{'cart_data':'','totalitems':0,'total_amt':total_amt})
            
# Add to cart
def addtocart(request):
	# del request.session['cartdata']
	cart_p={}
	cart_p[str(request.GET['id'])]={
		'image':request.GET['image'],
		'title':request.GET['title'],
		'quan':request.GET['qty'],
		'price':request.GET['price'],
	}
	if 'cartdata' in request.session:
		if str(request.GET['id']) in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['quan']=int(cart_p[str(request.GET['id'])]['quan'])
			cart_data.update(cart_data)
			request.session['cartdata']=cart_data
		else:
			cart_data=request.session['cartdata']
			cart_data.update(cart_p)
			request.session['cartdata']=cart_data
	else:
		request.session['cartdata']=cart_p
	return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

# Delete Cart Item
def removecart(request):
	pid=str(request.GET['id'])
	if 'cartdata' in request.session:
		if pid in request.session['cartdata']:
			cart_data=request.session['cartdata']
			del request.session['cartdata'][pid]
			request.session['cartdata']=cart_data
	total_amt=0
	for pid,item in request.session['cartdata'].items():
		total_amt+=int(item['quan'])*float(item['price'])
    
	t=render_to_string('ajax/cart.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'totalamount':total_amt,'finalamount':total_amt+70})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})

#update cart
def updatecart(request):
	p_id=str(request.GET['id'])
	p_qty=request.GET['qty']
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['quan']=p_qty
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['quan'])*float(item['price'])
	t=render_to_string('ajax/cart.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'totalamount':total_amt,'finalamount':total_amt+70})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})

    #checkout
@login_required
def checkout(request):
    totalamount = 0
    for pid,item in request.session['cartdata'].items():
        totalamount += int(item['quan'])*float(item['price'])         
    userprofile = CustomerProfile.objects.filter(user=request.user).first()        
    return render(request, 'checkout/checkout.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'totalamount':totalamount+70,'up':userprofile})

@login_required
def place_order(request):
    totalamount = 0
    if request.method == 'POST':
        if not CustomerProfile.objects.filter(user=request.user):
                userprofile = CustomerProfile()
                userprofile.user = request.user
                userprofile.phone = request.POST.get('phone')
                userprofile.state = request.POST.get('state')
                userprofile.city = request.POST.get('city')
                userprofile.address = request.POST.get('address')
                userprofile.save()
        
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.state = request.POST.get('state')
        neworder.city = request.POST.get('city')
        neworder.address = request.POST.get('address')
        neworder.payment_type = request.POST.get('payment_type')
        for pid,item in request.session['cartdata'].items():
            totalamount += int(item['quan'])*float(item['price'])
        # print("wtf"+str(finalamount))
        neworder.total_price = totalamount + 70

        track_number = str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_number=track_number) is None:
            track_number = str(random.randint(1111111,9999999))
        neworder.tracking_number = track_number
        neworder.save()

        customer = CustomerProfile.objects.get(user=request.user)
        print(customer)
        for pid,item in request.session['cartdata'].items():
            totalamount += int(item['quan'])*float(item['price'])
            print("rijan"+str(pid))
            products = Product.objects.get(id=pid)
            #order items
            items = OrderItem.objects.create(
                order = neworder,
                user = request.user,
                product = products,
                price = item['price'],
                quantity = item['quan']
            )
        
    del request.session['cartdata']
    messages.success(request,'Your order has been succesfully placed')
    return redirect("/sendemail/"+str(neworder.id))

@login_required
def order(request):
    op = OrderItem.objects.filter(user=request.user).order_by('-order')
    return render(request, 'order/order.html',{'order_placed':op,'activec':'btn-success'})

#address
@login_required
def address(request):
    if request.user.is_authenticated:
        address = CustomerProfile.objects.filter(user=request.user)
        if address:
            return render(request, 'address/address.html', {'add':address ,'activeb':'btn-success'})
        else:
            return redirect('create-address')

#create address
@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        form = CustomerAddressForm()
        return render(request, 'address/createAddress.html', {'form':form, 'activeb':'btn-success'})
    
    def post(self, request):
        form = CustomerAddressForm(request.POST)
        duplicateEntry = CustomerProfile.objects.filter(user=request.user)
        count = 0
        check = duplicateEntry.count()
        if check > 0:
            count = count + 1
        if form.is_valid():
            if count == 0: 
                usr = request.user
                state = form.cleaned_data['state']
                city = form.cleaned_data['city']
                address = form.cleaned_data['address']
                phone = form.cleaned_data['phone']
                reg = CustomerProfile(user=usr, state=state, city=city, address=address, phone=phone)
                reg.save()
                messages.success(request, 'Congratulations!! Profile Created Successfully')
            else:
                messages.warning(request, 'Profile Already Created')
        return redirect('address')
        context = {
            'form':form,
            'active':'btn-success'
        }
        return render(request, 'address/createAddress.html', context)

#edit address
@login_required    
def edit_address(request, pk):
    user_profile = CustomerProfile.objects.get(id=pk)
    form = CustomerAddressForm(instance=user_profile)
    if request.method == "POST":
        form = CustomerAddressForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('address')
    context = {
        'form':form,
        'activeb':'btn-success',
    }
    return render(request, 'address/editAddress.html', context)

#delete address
@login_required
def delete_address(request, pk):
    user_profile = CustomerProfile.objects.filter(id=pk)
    user_profile.delete()
    messages.success(request, 'Address Deleted Successfully')
    return redirect('address')

#search
def search(request):
    q = request.GET['q']
    data = Product.objects.filter(title__icontains=q).order_by('-id')#-id descending filter
    context = {
            'data':data
    }
    return render(request, 'search.html', context)

@login_required
def sendemail(request,tid):
    templatepath = 'order/ordermail.html'
    admintemplatepath = 'order/orderadminmail.html'
    print(tid)
    op = OrderItem.objects.filter(order=tid)
    print("udibabababa"+str(op))
    totamnt = 0
    for o in op:
        totamnt = o.order.total_price
    useremail = User.objects.filter(username=request.user)
    for b in useremail:
        uemail = b.email
        print("useremail"+uemail)
    context={'order':op,'tot':totamnt}
    template = get_template(templatepath)
    html = template.render(context)
    admintemplate = get_template(admintemplatepath)
    htmladmin = admintemplate.render(context)
    email_subject = "Your Order has been placed"
    email_adminsubject = "Order has been made by the user"
    email_body = html
    email_bodyadmin = htmladmin
    emails = EmailMessage(
        email_subject,
        email_body,
        'noreply@semycolon.com',
        [uemail],
    )
    emailsadmin = EmailMessage(
        email_adminsubject,
        email_bodyadmin,
        'noreply@semycolon.com',
        ['udibaba9741@gmail.com'],
    )
    emailsadmin.content_subtype = 'html'
    emailsadmin.send(fail_silently=False)
    emails.content_subtype = 'html'
    emails.send(fail_silently=False)#error dekhaune ho vane we do this
    #error dekhaune ho vane we do this
    response = redirect("order")
    return response

class load_more(View):
    def get(self, request):
        start=int(request.GET['curproducts'])
        limit=int(request.GET['limit'])
        prods = Category.objects.all().order_by('id')[start:start+limit]#fetch the latest product according to category with order_by,[:3]fetches first 3 products only
        t = render_to_string('ajax/menu.html',
        {
            'menulist':prods,
        })
        return JsonResponse({'datas':t})
