from django.contrib import admin
from django.contrib import admin
from .models import(
    Banner,
    Gallery,
)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext', 'img')
admin.site.register(Banner,BannerAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Gallery, GalleryAdmin)
