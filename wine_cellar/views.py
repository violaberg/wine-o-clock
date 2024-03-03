from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm
from .forms import SignupForm
from .models import GalleryImage
from .models import TourBooking
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
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'wine_cellar/login.html', {'form': form})


def book_a_tour(request):
    if request.method == 'POST':
        tour_date = request.POST.get('tour_date')
        num_guests = request.POST.get('num_guests')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Save the booking to the database
        TourBooking.objects.create(
            tour_date=tour_date,
            num_guests=num_guests,
            name=name,
            email=email,
            phone=phone
        )

        return redirect('book_a_tour_success')

    return render(request, 'wine_cellar/book_a_tour.html')


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
