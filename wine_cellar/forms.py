from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'message': 'Message',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'placeholder':'Enter your message here'}),
        }


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter a strong password')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Please repeat your password')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=254, help_text='Please enter a valid email address')
    password = forms.CharField(widget=forms.PasswordInput)
    

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, help_text='Please enter email address you used to register')