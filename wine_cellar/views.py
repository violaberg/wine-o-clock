from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm, ContactForm
from .models import GalleryImage
from .models import Review


def home(request):
    """
    Render the homepage.
    """
    return render(request, 'index.html')


def about(request):
    """
    Render the about page.
    """
    return render(request, 'wine_cellar/about.html')


def contact(request):
    """
    Handle contact form submission.

    Renders the contact form page and processes form submission.
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
    """
    gallery_images = GalleryImage.objects.all()
    return render(
        request, 'wine_cellar/gallery.html', {
            'gallery_images': gallery_images})


def display_review(request):
    """
    Display all reviews.
    """
    reviews = Review.objects.all()
    return render(request, 'wine_cellar/reviews.html', {'reviews': reviews})


def write_review(request, slug):
    """
    Handle writing a new review.

    Renders the reviews page with a review form for writing a new review.
    Handles form submission for creating a new review.
    """
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.author = request.user
            new_review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('display_review')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        review_form = ReviewForm()

    reviews = Review.objects.all()

    return render(
        request,
        'wine_cellar/reviews.html',
        {'reviews': reviews,
         'review_form': review_form}
    )


def edit_review(request, slug, review_id):
    """
    Handle editing reviews.
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid() and review.author == request.user:
            review_form.save()
            messages.success(
                request, messages.SUCCESS, 'Review updated successfully!')
            return redirect('display_review')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!')
            return redirect('reviews')

    return HttpResponseRedirect(reverse('display_review', args=[slug]))


def delete_review(request, slug, review_id):
    """
    Handle deleting reviews.
    """
    review = get_object_or_404(Review, pk=review_id)
    if review.author == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('display_review', args=[slug]))
