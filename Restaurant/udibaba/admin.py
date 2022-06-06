from django.contrib import admin
from .models import(
    Banner,
    Video,
    Product,
    Category,
    Gallery,
    Event,
    Contact,
    Cart
)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext', 'img')
admin.site.register(Banner,BannerAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Gallery, GalleryAdmin)


admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(Cart)
