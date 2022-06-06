from django.contrib import admin
from .models import(
    Banner,
    Video,
    Product,
    Category,
    Gallery,
    Event,
    Contact
)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext', 'img',)
admin.site.register(Banner,BannerAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Gallery, GalleryAdmin)


admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Event)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
admin.site.register(Contact, ContactAdmin)