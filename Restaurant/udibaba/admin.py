from django.contrib import admin
<<<<<<< HEAD
from .models import Banner,Video,Product,Category
=======
from .models import Banner
>>>>>>> origin/rijanbranch
from django.contrib import admin
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext','img')
admin.site.register(Banner,BannerAdmin)
<<<<<<< HEAD

admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Product)
=======
>>>>>>> origin/rijanbranch
