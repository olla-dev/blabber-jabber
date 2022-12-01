from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from django.dispatch import receiver

from users.models import Profile, ImageModel

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        avatar = ImageModel()
        avatar.get_image_from_url('http://i.stack.imgur.com/PIFN0.jpg')
        avatar.save()
        Profile.objects.create(user=instance, avatar=avatar)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    print('User just logged in....')
    user.profile.online = True
    user.profile.save()

    # broadcast user online
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('chat', {
        'type': 'user_status_update',
        'command': 'user_status_update',
        'online': 1,
        'user': user.id
    })


@receiver(user_logged_out)
def post_login(sender, user, request, **kwargs):
    print('User just logged out....')
    user.profile.online = False
    user.profile.save()

    # broadcast user offline
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('chat', {
        'type': 'user_status_update',
        'command': 'user_status_update',
        'online': 0,
        'user': user.id
    })