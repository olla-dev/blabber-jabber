from rest_framework import serializers
from .serializers import *
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    '''Represents a Chat Message'''
    chat_room_id = serializers.IntegerField(source='room.id', required=False, read_only=True)
    author_id = serializers.IntegerField(source='author.id', required=False, read_only=True)

    class Meta:
        model = Message
        fields = (
            'id',
            'content',
            'status',
            'chat_room_id',
            'author_id',
            'sent_time_utc',
        )