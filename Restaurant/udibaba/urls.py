from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
     path('', views.home, name='home'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('review/', views.review, name='review'),
     path('menu/', views.menu, name='menu'),
     path('profile/', views.profile, name='profile'),
     path('gallery/', views.gallery, name='gallery'),
     #registration and login
     path('signup/', views.signup, name='signup'),
     path('login/', views.login_view, name='login'),
     path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
     #start of password change
     path('password-change/', auth_views.PasswordChangeView.as_view(template_name = 'user/change-password/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/password-change-successfully/'), name='passwordchange'),
     path('password-change-successfully/', auth_views.PasswordChangeDoneView.as_view(template_name = 'user/change-password/passwordchangesuccessfully.html'), name='passwordchangesuccessfully'),
     #start of reset password
     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/reset-password/password_reset.html', form_class=MyPasswordResetForm, success_url='/password-reset-sent/'), name='password_reset'),
     path('password-reset-sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/reset-password/password_reset_sent.html'), name='password_reset_sent'),
     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/reset-password/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/reset-password/password_reset_complete.html'), name='password_reset_complete'),
     #start of resend otp
     path('resendOTP', views.resend_otp),
     #reviews
     path('submit-review/', views.submit_review, name='submit_review'),
     #start of cart
     path('cart/',views.cart_list,name='cart'),
     path('addtocart/', views.addtocart, name='addtocart'),
     path('removecart/',views.removecart,name='removecart'),
     path('updatecart/',views.updatecart,name='updatecart'),
     #start of checkout
     path('checkout/',views.checkout,name='checkout'),
     path('menulist/<int:pk>', views.menulist, name='menulist'),
     path('place-order/', views.place_order, name='placeorder'),
     path('order/', views.order, name='order'),
     #start of address
     path('address/', views.address, name='address'),
     path('create-address/', views.AddressView.as_view(), name='create-address'),
     path('edit-address/<str:pk>', views.edit_address, name='edit-address'),
     path('delete-address/<str:pk>', views.delete_address, name='delete-address'),
]