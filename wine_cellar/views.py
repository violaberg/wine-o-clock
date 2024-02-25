from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import GalleryImage


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