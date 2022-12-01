from django.db import models
from django.contrib.auth.models import User
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class ImageModel(models.Model):
    img = models.ImageField(upload_to='images', null = True)
    img_url = models.URLField(blank=True, null=True)
    
    def get_image_from_url(self, url):
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(url) as uo:
            assert uo.status == 200
            img_tmp.write(uo.read())
            img_tmp.flush()
        img = File(img_tmp)
        self.image.save(img_tmp.name, img)
        self.image_url = url

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

