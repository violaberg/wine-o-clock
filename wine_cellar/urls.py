from django.urls import path
from . import views
from .views import home
from .views import about
from .views import contact
from .views import gallery


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path(
     'contact_form_success/',
     views.contact_form_success,
     name='contact_form_success'),
    path('gallery/', gallery, name='gallery'),
    path('reviews', views.reviews, name='reviews'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.delete_review, name='delete_review'),
]
