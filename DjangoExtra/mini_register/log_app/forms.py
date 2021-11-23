# Inside your app's forms.py file
from django import forms
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class RegisterForm(UserCreationForm):
#from django.forms import ModelForm
  class Meta:
      model = User
      fields = ['first_name', 'last_name', 'username', 'email']
# class RegisterForm(forms.Form):
#     first_name = forms.CharField(label = anything you want for label, max_length=45)
#     last_name = forms.CharField(max_length=45)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
class LoginForm(AuthenticationForm):
  class Meta: #it can be place which specify which label , input or class we use
      model = User
      fields = '__all__'
