from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary_storage.storage import RawMediaCloudinaryStorage


# Recipe Model
class Recipe(models.Model):
    headline = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = models.TextField()
    preparation = models.TextField()
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    liked_by = models.ManyToManyField(User, related_name='liked_recipes')
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='recipe_images', max_length=200,
        storage=RawMediaCloudinaryStorage())

# Method to get the count of likes for the recipe
    def get_likes_count(self):
        return self.liked_by.count()

# String representation of the Recipe object
    def __str__(self):
        return self.headline


# Profile Model for storing user's profile information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    favorite_recipes = models.ManyToManyField(
        Recipe, related_name='favorited_by')
    profile_image = CloudinaryField('profile_images', null=True, blank=True)

# String representation of the Profile object
    def __str__(self):
        return self.user.username


# Signal to create a user profile when a User object is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Signal to save a user profile when a User object is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# Create your models here.
