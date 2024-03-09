from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Contact model
class Contact(models.Model):
    """
    Represents a contact form submission.

    Attributes:
        first_name (CharField): The first name of the person submitting the form.
        last_name (CharField): The last name of the person submitting the form.
        email (EmailField): The email address of the person submitting the form.
        message (TextField): The message submitted through the form.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Gallery model
class GalleryImage(models.Model):
    """
    Represents an image in the gallery.

    Attributes:
        image (ImageField): The image field for storing the image.
        description (TextField): The description of the gallery image.
    """
    image = models.ImageField(upload_to="gallery/")
    description = models.TextField()

    def __str__(self):
        return f"Image {self.id}"


# Booking model
class TourBooking(models.Model):
    """
    Represents a booking for a wine cellar tour.

    Attributes:
        tour_date (DateTimeField): The date and time of the tour.
        num_guests (IntegerField): The number of guests for the tour.
        name (CharField): The name of the person booking the tour.
        email (EmailField): The email address of the person booking the tour.
        phone (IntegerField): The phone number of the person booking the tour.
    """
    tour_date = models.DateTimeField()
    num_guests = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.name} on {self.tour_date}"


# Review model
class Review(models.Model):
    """
    Represents a review written by a user for a wine cellar tour.

    Fields:
        - author (ForeignKey to User): The user who wrote the review.
        - body (TextField): The textual content of the review.
        - image (ImageField): An optional image attached to the review.
        - timestamp (DateTimeField): The date and time when the review was created.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"Review {self.body} {self.image.url if self.image else ''} by {self.author}"