# Generated by Django 4.2.10 on 2024-03-14 10:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_cellar', '0006_rename_image_review_review_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryimage',
            old_name='image',
            new_name='gallery_image',
        ),
        migrations.AlterField(
            model_name='review',
            name='review_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]