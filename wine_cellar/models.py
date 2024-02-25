from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField()

    def __str__(self):
        return f"Image {self.id}"
