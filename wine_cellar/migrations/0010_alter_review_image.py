# Generated by Django 4.2.10 on 2024-03-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine_cellar', '0009_alter_galleryimage_image_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery/'),
        ),
    ]
