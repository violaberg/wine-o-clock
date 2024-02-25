from django.urls import path
from .views import home
from .views import about
from .views import contact
from .views import gallery

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
]