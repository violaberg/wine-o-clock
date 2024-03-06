from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm
from .forms import SignupForm
from .models import GalleryImage
from .models import TourBooking
from .forms import TourBookingForm
from .forms import LoginForm
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'wine_cellar/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Send confirmation email
            subject = 'Thank you for contacting us!'
            message = 'We have received your message and will get back to you soon.'
            from_email = 'viola.bergere@gmail.com'
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, from_email, recipient_list)

            # Confirmation of form submitted successfully
            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
    else:
        form = ContactForm()

    return render(request, 'wine_cellar/contact.html', {'form': form})


def gallery(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'wine_cellar/gallery.html', {'gallery_images': gallery_images})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'wine_cellar/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm(request)
    return render(request, 'wine_cellar/login.html', {'form': form})


def book_a_tour(request):
    if request.method == 'POST':
        form = TourBookingForm(request.POST)
        if form.is_valid():
            # Save the booking to the database
            tour_booking = form.save()

            # Send confirmation email
            send_confirmation_email(tour_booking.name, tour_booking.email, tour_booking.tour_date)

            return redirect('book_a_tour_success')
        else:
            # Form is not valid, handle accordingly
            return render(request, 'wine_cellar/book_a_tour.html', {'form': form})

    else:
        # GET request, render the form
        form = TourBookingForm()

    return render(request, 'wine_cellar/book_a_tour.html', {'form': form})


def book_a_tour_success(request):
    return render(request, 'wine_cellar/book_a_tour_success.html')


def send_confirmation_email(name, email, tour_date):
    subject = 'Wine Cellar Tour Booking Confirmation'
    message = f'Thank you, {name}, for booking a wine tour with us on {tour_date}. We look forward to welcoming you!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


@login_required
def write_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('book_a_tour')

    else:
        review_form = ReviewForm()

    reviews = Review.objects.filter(user=request.user)

    return render(request, 'wine_cellar/book_a_tour.html', {'review_form': review_form, 'reviews': reviews})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('book_a_tour')

    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'wine_cellar/edit_review.html', {'review_form': review_form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('book_a_tour')

    return render(request, 'wine_cellar/delete_review.html', {'review': review})
