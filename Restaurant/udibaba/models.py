from django.db import models
from django.utils.html import mark_safe

class Banner(models.Model):
  img = models.ImageField(upload_to='banner_imgs/')
  headertext = models.CharField(max_length=300)
  subtext = models.CharField(max_length=300)

<<<<<<< HEAD
  def image_tag(self):
    return mark_safe('img src="%s" width="50" />' % (self.img.url))

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
=======
def image_tag(self):
    return mark_safe('img src="%s" width="50" />' % (self.img.url))

def __str__(self):
    return str(self.id)+ " " + str(self.headertext)
>>>>>>> origin/rijanbranch
