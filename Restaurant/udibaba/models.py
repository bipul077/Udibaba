from django.db import models
from django.utils.html import mark_safe
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from numpy import False_
from django.template.loader import get_template

class Banner(models.Model):
  img = models.ImageField(upload_to='banner_imgs/')
  headertext = models.CharField(max_length=300)
  subtext = models.CharField(max_length=300)
  def image_tag(self):
    return mark_safe('<img src="%s" width="50" height="50" />'%(self.img.url))
  def __str__(self):
    return str(self.id)+ " " + str(self.headertext)

class Video(models.Model):
  title = models.CharField(max_length=100)
  caption = models.CharField(max_length=100)

  def __str__(self):
    return str(self.id)+ " " + str(self.title)

class Category(models.Model):
  title = models.CharField(max_length=100)
  img = models.ImageField(upload_to='category_imgs/',default='')

  def image_tag(self):
    return mark_safe('<img src="%s" width="50" height="50" />'%(self.img.url))

  def __str__(self):
    return str(self.title)

class Product(models.Model):
  title = models.CharField(max_length=100)
  item_price = models.FloatField()
  description = models.TextField()
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  product_image = models.FileField(upload_to='img/%m', blank = True,null=True)
  is_featured = models.BooleanField(default=False)
  def __str__(self):
    return str(self.id) + " " + str(self.title)

class Gallery(models.Model):
  title = models.CharField(max_length=50, unique=False)
  description = models.CharField(max_length=150)
  image = models.ImageField(upload_to='gallery_imgs/',default="default.jpg")
  def __str__(self):  
    return self.title 

  @property
  def image_count(self):
      return self.multiplegalleryimage_set.count()

class Multiplegalleryimage(models.Model):
  gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
  images = models.FileField(upload_to = 'gallery_imgs/')
  

class Event(models.Model):
  title = models.CharField(max_length=30, unique=False)
  description = models.CharField(max_length=250)
  date = models.DateTimeField(default=datetime.now, blank=True)
  image = models.ImageField(upload_to='event_imgs/',default="default.jpg")
  def __str__(self):  
    return self.title 

class Contact(models.Model):
  uname = models.CharField(max_length=200)
  email =  models.CharField(max_length=200)
  message = models.TextField()

  def __str__(self):
    return self.uname

#For OTP    
class UserOTP(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  time_st = models.DateTimeField(auto_now = True)
  otp = models.IntegerField()
  
#Review
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
  
# Order
ORDER_STATUS=(
  ('cancelled','Cancelled'),
  ('on the way','On The Way'),
  ('delivered','Delivered'),
)

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  fname = models.CharField(max_length=150, null=False)
  lname = models.CharField(max_length=150, null=False)
  email = models.CharField(max_length=150, null=False)
  phone = models.CharField(max_length=150, null=False)
  state = models.CharField(max_length=150, null=False)
  city = models.CharField(max_length=150, null=False)
  address = models.CharField(max_length=150, null=False)
  total_price = models.PositiveIntegerField(null=False)
  payment_type = models.CharField(max_length=100, null=False)
  status = models.CharField(max_length=50, choices=ORDER_STATUS,default='Pending')
  message = models.TextField(null=True)
  tracking_number = models.CharField(max_length=100, null=True)
  ordered_date = models.DateTimeField(default=now)
  updated_date = models.DateTimeField(auto_now=True)
  payment_completed = models.BooleanField(default=False, null=True, blank=True)
  def __str__(self):
      # return '{} - {}'.format(self.id, self.tracking_number)
      return self.tracking_number
  
STATE_CHOICES = (
    ('Bagmati Province', 'Bagmati Province'),
)

class CustomerProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=10, null=False)
  state = models.CharField(choices = STATE_CHOICES, max_length=50)
  city = models.CharField(max_length=50, null=False)
  address = models.CharField(max_length=50, null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.user.username 

# OrderItems
class OrderItem(models.Model):
  user = models.CharField(max_length=50, null=False)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  price = models.FloatField(null=False)
  quantity = models.IntegerField(null=False)
  
  def __str__(self):
      return '{} - {}'.format(self.order.id, self.order.tracking_number)
  
  class Meta:
    verbose_name_plural='Order Items'

  def image_tag(self):
    return mark_safe('<img src="%s" width="30" height="30" />'%(self.image))

class Deliverycharge(models.Model):
  title = models.CharField(max_length=20,null=False,default="KTM")
  Deliverycost = models.FloatField(null=False)

  def __str__(self):
    return self.title

class AdHeader(models.Model):
  Info = models.CharField(max_length=50,null=True,blank=True)
  addesc = models.CharField(max_length=70,null=True,blank=True)

  def __str__(self):
    return self.Info

class Multipleadimage(models.Model):
  prod = models.ForeignKey(AdHeader, default=None, on_delete=models.CASCADE)
  images = models.ImageField(upload_to = 'img/ad')
  addesc = models.CharField(max_length=20,null=True,blank=True)
  link = models.CharField(max_length=100,null=True,blank=True)
  def __str__(self):
        return self.prod.Info 

@receiver(post_save, sender=Order)
def create_user_profile(sender, instance, created, **kwargs):
    if created == False:
      templatepath = 'order/ordermail.html'
      print("asdfasdf ",instance.email, instance.status)
      op = OrderItem.objects.filter(order=instance.id)
      print("ohyes")
      print(op)
      context={'order':op,'tot':instance.total_price,'mes':instance.message,'status':instance.status}
      template = get_template(templatepath)
      html = template.render(context)
      email_subject = "Your Order has been " + instance.status
      email_body = html
      emailsed = EmailMessage(
        email_subject,
        email_body,
        'noreply@semycolon.com',
        [instance.email],
      )
      emailsed.content_subtype = 'html'
      emailsed.send(fail_silently=False)
 
 
