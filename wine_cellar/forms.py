from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from .models import Review
from .models import TourBooking


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
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required',
        widget=forms.CharField(attrs={'id': 'first_name', 'autocomplete': 'first_name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required',
        widget=forms.TextInput(attrs={'id': 'last_name', 'autocomplete': 'last_name'})
    )
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Please enter a valid email address')
    new_password = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter a strong password')
    repeat_password = forms.TextInput(widget=forms.PasswordInput, help_text='Required. Please repeat your password')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'new_password', 'repeat_password')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete': 'email'})

    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']
    

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, help_text='Please enter email address you used to register')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'text', 'image']
        widgets = {
            'user': forms.HiddenInput(),
        }


class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['tour_date', 'num_guests', 'name', 'email', 'phone']
        widgets = {
            'tour_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }