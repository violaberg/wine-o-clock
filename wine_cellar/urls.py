from django.urls import path
from .views import home
from .views import about
from .views import contact
from .views import gallery
from .views import book_a_tour, book_a_tour_success


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('book_a_tour/', book_a_tour, name='book_a_tour'),
    path('book_a_tour_success/', book_a_tour_success, name='book_a_tour_success'),
]