from django.urls import path
from . import views
from .views import home
from .views import about
from .views import contact
from .views import gallery
from .views import display_review
from .views import edit_review


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('reviews/', display_review, name='display_review'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.edit_review, name='edit_review'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.delete_review, name='delete_review'),
]