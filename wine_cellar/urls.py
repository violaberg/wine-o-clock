from django.urls import path
from .views import home
from .views import about
from .views import contact, contact_form_success
from .views import gallery
from .views import reviews


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('reviews/', reviews, name='reviews'),
    path('contact_form_success/', contact_form_success, name='contact_form_success'),
]