from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import ContactForm
from .forms import ReviewForm
from .models import GalleryImage
from .models import Review


# Create your views here.
def home(request):
    """
    Render the homepage.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the homepage template.
    """
    return render(request, 'index.html')


def about(request):
    """
    Render the about page.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the about page template.
    """
    return render(request, 'wine_cellar/about.html')


def contact(request):
    """
    Handle contact form submission.

    Renders the contact form page and processes form submission.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the contact form page or success page upon successful form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'wine_cellar/contact_form_success.html')

    else:
        form = ContactForm()
        return render(request, 'wine_cellar/contact.html', {'form': form})


def gallery(request):
    """
    Render the gallery page with all gallery images.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the gallery page with gallery images.
    """
    gallery_images = GalleryImage.objects.all()
    return render(request, 'wine_cellar/gallery.html', {'gallery_images': gallery_images})


def display_review(request):
    """
    Display all reviews.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the reviews page with all reviews.
    """
    reviews = Review.objects.all()
    return render(request, 'wine_cellar/reviews.html', {'reviews': reviews})


def write_review(request, slug):
    """
    Handle writing a new review.

    Renders the reviews page with a review form for writing a new review.
    Handles form submission for creating a new review.

    Args:
        request: HttpRequest object.
        slug: The slug parameter if any.

    Returns:
        HttpResponse object rendering the reviews page with a review form or after successful form submission.
    """
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
    """
    Handle editing reviews.

    Args:
        request: HttpRequest object.
        slug: The slug parameter if any.
        review_id: The ID of the review to be edited.

    Returns:
        HttpResponse object redirecting to the reviews page after editing the review.
    """
    if request.method == 'POST':

        queryset = Review.objects.all
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.success(request, messages.SUCCESS, 'Review updated successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')
            return redirect('reviews')

    return HttpResponseRedirect(reverse('reviews', args=[slug]))


def delete_review(request, slug, review_id):
    """
    Handle deleting reviews.

    Args:
        request: HttpRequest object.
        slug: The slug parameter if any.
        review_id: The ID of the review to be deleted.

    Returns:
        HttpResponse object redirecting to the reviews page after deleting the review.
    """
    queryset = Review.objects.all
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('reviews', args=[slug]))
