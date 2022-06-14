from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Review, CustomerProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label = ("First Name"))
    last_name = forms.CharField(label = ("Last Name"))
    username = forms.EmailField(label = ("Email"))#username = email address
    
    class Meta:
	    model = User
	    fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

#Customer Details Update Form     
class CustomerDetailsUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label = ("First Name"))
    last_name = forms.CharField(label = ("Last Name"))
    username = forms.EmailField(label = ("Email"))#username = email address
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        
#Password Change Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password "), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True}))
    new_password1 = forms.CharField(label=_("New Password "), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password "), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    
#Password Reset Form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email'}))

#Password Set Form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password "), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password "), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))

#Customer Review Form    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'review', 'rating']

#Customer Address Form
class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['state', 'city', 'address', 'zipcode', 'phone']
        widgets = {'state':forms.Select(), 'city':forms.TextInput(), 'address':forms.TextInput(), 'zipcode':forms.TextInput(), 'phone':forms.TextInput()}
        