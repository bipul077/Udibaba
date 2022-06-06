from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class SignUpForm(UserCreationForm):
    fullname = forms.CharField(label = ("Full Name"))
    username = forms.CharField(label = ("User Name"))
    email = forms.EmailField(label = ("Email")) 
    
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']
        
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