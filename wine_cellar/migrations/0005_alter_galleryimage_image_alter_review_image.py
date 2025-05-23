# Generated by Django 4.2.10 on 2024-03-14 09:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_cellar', '0004_contact_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=cloudinary.models.CloudinaryField(
                default='placeholder',
                max_length=255,
                verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=cloudinary.models.CloudinaryField(
                default='placeholder',
                max_length=255,
                verbose_name='review_image'),
        ),
    ]
