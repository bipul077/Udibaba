from django.db import models
from django.utils.html import mark_safe

class Banner(models.Model):
  img = models.ImageField(upload_to='banner_imgs/')
  headertext = models.CharField(max_length=300)
  subtext = models.CharField(max_length=300)

def image_tag(self):
      return mark_safe('img src="%s" width="50" />' % (self.img.url))

def __str__(self):
    return str(self.id)+ " " + str(self.headertext)

class Gallery(models.Model):
  title = models.CharField(max_length=50, unique=False)
  description = models.CharField(max_length=150)
  image = models.ImageField(upload_to='gallery_imgs/',default="default.jpg")
  def __str__(self):  
    return self.title 