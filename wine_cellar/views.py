from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, reverse
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
            return render(request, 'wine_cellar/contact_form_success.html')

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
    """
    View to edit reviews
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
    View to delete review
    """
    queryset = Review.objects.all
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('reviews', args=[slug]))
