from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import(
    Banner,
    CustomerProfile,
    Video,
    Product,
    Category,
    Gallery,
    Event,
    Contact,
    Review,
    Order,
    OrderItem
)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext', 'img','image_tag')
admin.site.register(Banner,BannerAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Gallery, GalleryAdmin)

admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Event)
admin.site.register(CustomerProfile)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
admin.site.register(Contact, ContactAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'created_at', 'updated_at')
admin.site.register(Review, ReviewAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address','status')
admin.site.register(Order, OrderAdmin)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product','price','quantity','customer_info')
    def customer_info(self,obj):
        link = reverse("admin:udibaba_customerprofile_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.user)
