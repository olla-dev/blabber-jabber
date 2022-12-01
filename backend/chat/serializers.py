from rest_framework import serializers
from .serializers import *
from users.serializers import UserSerializer
from .models import Message, ChatRoom

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


class ChatRoomSerializer(serializers.ModelSerializer):
    '''Represents a Chat room'''
    users = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = (
            'id',
            'name',
            'description',
            'users',
            'messages',
            'created_at',
            'updated_at',
        )

    def get_messages(self, obj):
        # get latest 10 messages
        messages = Message.objects.filter(room__id=obj.id).order_by('sent_time_utc')[:10]
        return MessageSerializer(messages, many=True).data