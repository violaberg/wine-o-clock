from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Contact model
class Contact(models.Model):
    """
    Represents a contact form submission.

    Attributes:
        first_name (CharField): The first name \
        of the person submitting the form.
        last_name (CharField): The last name \
        of the person submitting the form.
        email (EmailField): The email address \
        of the person submitting the form.
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
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer",
        max_length=30,
        default=''
    )
    body = models.TextField()
    image = CloudinaryField('image', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        review_body = self.body
        review_image = self.image.url if self.image else ''
        review_author = self.author

        return f"Review {review_body} {review_image} by {review_author}"
