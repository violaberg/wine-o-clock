from django import forms
from .models import Contact
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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'image')


class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['tour_date', 'num_guests', 'name', 'email', 'phone']
        widgets = {
            'tour_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }