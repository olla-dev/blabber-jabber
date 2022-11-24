from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class ImageModel(models.Model):
    name = models.TextField()
    img = models.ImageField(upload_to='images', null = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    age = models.IntegerField(null=True, blank=True)

    is_verified = models.BooleanField(default=False, editable=False)
    is_banned = models.BooleanField(default=False, editable=False)
    is_premium = models.BooleanField(default=False, editable=False)

    social_facebook = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_youtube = models.URLField(blank=True)
    social_blog = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

