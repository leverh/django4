# Generated by Django 3.2.19 on 2023-07-26 14:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_collection', '0003_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_images'),
        ),
    ]
