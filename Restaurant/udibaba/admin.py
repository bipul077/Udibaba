from django.contrib import admin
from .models import Banner,Video,Product,Category,Gallery
from .models import Banner
from django.contrib import admin
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext','img')
admin.site.register(Banner,BannerAdmin)

admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Gallery)