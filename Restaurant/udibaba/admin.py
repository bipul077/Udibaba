from django.contrib import admin
from .models import Banner
from django.contrib import admin
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext','img')
admin.site.register(Banner,BannerAdmin)
