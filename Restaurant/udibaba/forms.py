from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    fullname = forms.CharField(label = ("Full Name"))
    username = forms.CharField(label = ("User Name"))
    email = forms.EmailField(label = ("Email")) 
    
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']