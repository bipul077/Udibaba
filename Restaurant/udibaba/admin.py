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
    OrderItem,
    Deliverycharge
)
admin.site.register(Deliverycharge)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('headertext', 'img','image_tag')
admin.site.register(Banner,BannerAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
admin.site.register(Gallery, GalleryAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
admin.site.register(Video, VideoAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_featured')
    list_display_links = ('title',)
    list_editable = ('is_featured',)
admin.site.register(Product, ProductAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
admin.site.register(Event, EventAdmin)

class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user',)
admin.site.register(CustomerProfile, CustomerProfileAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email',)
admin.site.register(Contact, ContactAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'created_at', 'updated_at', 'status')
    list_display_links = ('user',)
    list_editable = ('status',)

admin.site.register(Review, ReviewAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address','status')
    list_display_links = ('user',)
admin.site.register(Order, OrderAdmin)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('customer_info','order', 'price','quantity')
    list_display_links = ('customer_info', 'order')
    def customer_info(self,obj):
        link = reverse("admin:udibaba_order_change",args=[obj.order.pk])
        return format_html('<a href="{}">{}</a>',link,obj.order.user.first_name + " " + obj.order.user.last_name)
