
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.cache import cache

from .models import ChatRoom

@receiver(m2m_changed, sender=ChatRoom.users.through)
def cart_update_total_when_item_added(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        print('ChatRoom update (add)')
        # update cache
        cached_rooms = cache.get("rooms")
        if cached_rooms:
            cached_rooms.append(instance)
            cache.set("rooms", cached_rooms)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('chat', {
            'type': 'chat_room_update',
        })

    if action == 'post_remove':
        print('ChatRoom update (remove)')
        # update cache
        cached_rooms = cache.get("rooms")
        if instance in cached_rooms:
            cache.delete("rooms")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('chat', {
            'type': 'chat_room_update',
        })