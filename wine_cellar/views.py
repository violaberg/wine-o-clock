from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .forms import ContactForm
from .models import GalleryImage
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
            messages.add_message(
                request,
                'Thank you for contacting us! We have received your message and will get back to you soon.')

    else:
        form = ContactForm()

    return render(request, 'wine_cellar/contact.html', {'form': form})


def gallery(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'wine_cellar/gallery.html', {'gallery_images': gallery_images})


def display_review(request):
    reviews = Review.objects.all()
    return render(request, 'wine_cellar/reviews.html', {'reviews': reviews})


def write_review(request, slug):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.author = request.user
            new_review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('reviews')

    else:
        review_form = ReviewForm()

    reviews = Review.objects.filter(author=request.user)
    print(reviews)

    return render(
        request,
        'wine_cellar/reviews.html',
        {'reviews': reviews,
         'review_form': review_form}
    )


def edit_review(request, slug, review_id):
    review = get_object_or_404(Review, slug=slug, id=review_id, author=request.user)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('reviews')

    else:
        review_form = ReviewForm(data=request.POST,instance=review)

    return render(request, 'wine_cellar/edit_review.html', {'review_form': review_form})


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('reviews')

    else:
        messages.add_message(
            request,
            messages.ERROR, 'You can only delete your own reviews!')

    return render(request, 'wine_cellar/delete_review.html', {'review': review})
