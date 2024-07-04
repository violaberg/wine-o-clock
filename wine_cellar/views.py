from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            send_contact_success_email(form.cleaned_data['email'])
            return redirect('contact_form_success')
        else:
            messages.error(
                request, 'An error occured. Please try again.')
    else:
        form = ContactForm()
        return render(request, 'wine_cellar/contact.html', {'form': form})


def contact_form_success(request):
    """
    Render the contact success page.
    """
    return render(request, 'wine_cellar/contact_form_success.html')


def send_contact_success_email(user_email):
    """
    Send a confirmation email to the user \
    upon successful contact form submission.

    Args:
        user_email (str): The email address of the user \
        who submitted the contact form.
    """
    subject = 'Contact Form Received'
    message_body = "Thank you for contacting us! \
                    We will get back to you as soon as possible!"
    signature = "\n\nSincerely yours,\nWine O'Clock!"
    message = f"{message_body}{signature}"
    from_email = 'viola.bergere@gmail.com'
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')


def gallery(request):
    """
    Render the gallery page with all gallery images.
    """
    gallery_images = GalleryImage.objects.all()
    return render(
        request, 'wine_cellar/gallery.html', {
            'gallery_images': gallery_images})


def reviews(request):
    """
    Display and handle reviews.

    This view function retrieves and displays all reviews, paginates them,
    handles new review submissions, and displays the review form. Only
    authenticated users can access this view.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object rendering the reviews page with
        the reviews, pagination object, and review form.
    """
    reviews = Review.objects.all().order_by('-timestamp')
    p = Paginator(reviews, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for your review!'
            )
            return redirect('reviews')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Something went wrong! Please try again.'
            )
    else:
        form = ReviewForm()

    context = {
        'reviews': reviews,
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'wine_cellar/reviews.html', context)


def delete_review(request, review_id):
    """
    Handle deleting reviews.
    """
    review = get_object_or_404(Review, pk=review_id)
    if review.author == request.user:
        review.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Review deleted!'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own reviews!'
        )

    return redirect('reviews')


def edit_review(request, review_id):
    """
    Handle editing reviews.
    """
    review = get_object_or_404(Review, pk=review_id)

    if review.author != request.user:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only edit your own reviews!'
        )
        return redirect('reviews')

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Review updated!'
            )
            return redirect('reviews')
    else:
        form = ReviewForm(instance=review)

    return render(
        request, 'reviews.html', {'form': form, 'review': review})
