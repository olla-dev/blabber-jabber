import os
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File  # you need this somewhere
import urllib
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class ImageModel(models.Model):
    img = models.ImageField(upload_to='images', null = True)
    img_url = models.URLField(blank=True, null=True)
    
    def get_image_from_url(self, url):
        self.img_url = url
        result = urllib.request.urlretrieve(url) 
        self.img.save(os.path.basename(self.img_url),
            File(open(result[0], 'rb'))
        )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.OneToOneField(ImageModel, on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.IntegerField(null=True, blank=True)

    online = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False, editable=False)
    is_banned = models.BooleanField(default=False, editable=False)
    is_premium = models.BooleanField(default=False, editable=False)

    social_facebook = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_youtube = models.URLField(blank=True)
    social_blog = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

