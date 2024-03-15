from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name}"


# Gallery model
class GalleryImage(models.Model):
    """
    Represents an image in the gallery.

    Attributes:
        image (ImageField): The image field for storing the image.
        description (TextField): The description of the gallery image.
    """
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return f"Image {self.id}"


# Review model
class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`

    Fields:
        - author (ForeignKey to User): The user who wrote the review.
        - body (TextField): The textual content of the review.
        - review_image (ImageField): An optional image attached to the review.
        - timestamp (DateTimeField): The date and time when the review was created.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer", max_length=30, default='')
    body = models.TextField()
    image = CloudinaryField('image', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"Review {self.body} {self.image.url if self.image else ''} by {self.author}"