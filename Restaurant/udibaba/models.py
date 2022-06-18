from django.db import models
from django.utils.html import mark_safe
from datetime import datetime
from django.contrib.auth.models import User

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

  def __str__(self):
    return str(self.title)

class Product(models.Model):
  title = models.CharField(max_length=100)
  item_price = models.FloatField()
  description = models.TextField()
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  product_image = models.FileField(upload_to='img/%m', blank = True)
  is_featured = models.BooleanField(default=False)
  def __str__(self):
    return str(self.id) + " " + str(self.title)
def image_tag(self):
      return mark_safe('<img src="%s" width="50" />' % (self.product_image))

def __str__(self):
    return str(self.id)+ " " + str(self.headertext)

class Gallery(models.Model):
  title = models.CharField(max_length=50, unique=False)
  description = models.CharField(max_length=150)
  image = models.ImageField(upload_to='gallery_imgs/',default="default.jpg")
  def __str__(self):  
    return self.title 

class Event(models.Model):
  title = models.CharField(max_length=50, unique=False)
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
  ('process','In Process'),
  ('shipped','Shipped'),
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
  zipcode = models.CharField(max_length=150, null=False)
  total_price = models.PositiveIntegerField(null=False)
  payment_type = models.CharField(max_length=100, null=False)
  status = models.CharField(max_length=50, choices=ORDER_STATUS,default='Pending')
  message = models.TextField(null=True)
  tracking_number = models.CharField(max_length=100, null=True)
  ordered_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  payment_completed = models.BooleanField(default=False, null=True, blank=True)
  def __str__(self):
      return '{} - {}'.format(self.id, self.tracking_number)



STATE_CHOICES = (
    ('Bagmati Province', 'Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
)

class CustomerProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=10, null=False)
  state = models.CharField(choices = STATE_CHOICES, max_length=50)
  city = models.CharField(max_length=50, null=False)
  address = models.CharField(max_length=50, null=False)
  zipcode = models.CharField(max_length=50, null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.user.username 

# OrderItems
class OrderItem(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  # customer = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  price = models.FloatField(null=False)
  quantity = models.IntegerField(null=False)
  
  def __str__(self):
      return '{} - {}'.format(self.order.id, self.order.tracking_number)
  
  class Meta:
    verbose_name_plural='Order Items'

  def image_tag(self):
    return mark_safe('<img src="%s" width="30" height="30" />'%(self.image))
