from django.urls import path
from .views import home
from .views import about
from .views import contact
from .views import gallery
from .views import display_review


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('reviews/', display_review, name='display_review'),
]