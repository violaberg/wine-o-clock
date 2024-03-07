from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils import timezone
from .forms import ContactForm
from .models import GalleryImage
from .models import TourBooking
from .forms import TourBookingForm
from .models import Review
from .forms import ReviewForm
from django.contrib import messages


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

            # Confirmation of form submitted successfully
            return JsonResponse({'success': True, 'message': 'Thank you for contacting us! We have received your message and will get back to you soon.'})
    else:
        form = ContactForm()

    return render(request, 'wine_cellar/contact.html', {'form': form})


def gallery(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'wine_cellar/gallery.html', {'gallery_images': gallery_images})


def book_a_tour(request):
    if request.method == 'POST':
        form = TourBookingForm(request.POST)
        if form.is_valid():
            # Save the booking to the database
            tour_booking = form.save()

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


def display_review(request):
    reviews = Review.objects.all()
    return render(request, 'wine_cellar/book_a_tour.html', {'reviews': reviews})


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
    print(reviews)

    return render(request, 'wine_cellar/book_a_tour.html', {'review_form': review_form, 'reviews': reviews})


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


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('book_a_tour')

    return render(request, 'wine_cellar/delete_review.html', {'review': review})
