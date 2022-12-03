
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.cache import cache
from functools import wraps
from chat.serializers import MessageSerializer


from .models import ChatRoom, Message

@receiver(m2m_changed, sender=ChatRoom.users.through)
def room_users_update(sender, instance, action, *args, **kwargs):
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
        # reset cache
        cache.delete("rooms")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('chat', {
            'type': 'chat_room_update',
        })

@receiver(post_save, sender=Message)
def save_message(sender, instance, **kwargs):
    # unset cache on new message
    cache.delete(f"room_{instance.id}_messages")

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('chat', {
        'type': 'chat_room_update',
        'command': 'chat_room_update',
        'room_id': instance.room.id,
        'message': MessageSerializer(instance, many=False).data
    })