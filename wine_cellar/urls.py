from django.urls import path
from .views import home
from .views import about
from .views import contact
from .views import gallery
from .views import signup, user_login
from .views import book_a_tour, book_a_tour_success
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('book_a_tour/', book_a_tour, name='book_a_tour'),
    path('book_a_tour_success/', book_a_tour_success, name='book_a_tour_success'),
    path('logout/', LogoutView.as_view(), name='logout'),
]