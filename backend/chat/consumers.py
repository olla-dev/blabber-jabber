import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from chat.models import ChatRoom
from chat.serializers import ChatRoomSerializer
from django.contrib.auth.models import User

class ChatEventConsumer(AsyncJsonWebsocketConsumer):
    '''This consumer handles general user events'''
    
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None

    @database_sync_to_async
    def join_room(self, room_name, user_id): 
        room = ChatRoom.objects.filter(name=room_name).first()
        if not room: 
            room = ChatRoom()
            room.name = room_name
            room.save()
        
        user = User.objects.filter(id=user_id).first()
        room.users.add(user)
        room.save()
        room_json = ChatRoomSerializer(room, many=False).data
        return room_json

    @database_sync_to_async
    def leave_room(self, room_id, user_id): 
        room = ChatRoom.objects.filter(id=room_id).first()
        if room: 
            user = User.objects.filter(id=user_id).first()
            room.users.remove(user)
            room.save()
            room_json = ChatRoomSerializer(room, many=False).data
            return room_json
        else:
            return None

    
    async def connect(self):
        self.model = 'chat'
        self.room_name = "home"

        await self.channel_layer.group_add(
            self.model, 
            self.channel_name
        )
        await self.accept()

        print("Connected!")
        self.send_json(
            {
                "type": "welcome_message",
                "message": "Hey there! You've successfully connected!",
            }
        )

    # Receive message from WebSocket
    def receive_json(self, content, **kwargs):
        print(content)
        return super().receive_json(content, **kwargs)
    
    async def receive_json(self, content, **kwargs):
        command = content["command"]
        user_id = content["user"]

        if not command: 
            self.send_json({
                "result": -1,
                "reason": "No command"
            })
        if not user_id:
            self.send_json({
                "result": -1,
                "reason": "No user provided"
            })

        # handle command
        if command == "join":
            # user joins the chat room
            room_name = content["room"]
            room = await self.join_room(room_name, user_id)
            
            await self.send(text_data=json.dumps({
                'command': command,
                'result': 0,
                'room': room
            }))

        if command == "leave":
            # user joins the chat room
            room_id = content["room"]
            room = await self.leave_room(room_id, user_id)
            print(room)
            if room: 
                await self.send(text_data=json.dumps({
                    'command': command,
                    'result': 0,
                    'room': room
                }))
            else:
                await self.send(text_data=json.dumps({
                    "result": -2,
                    "reason": "Leave room failed"
                }))

        return super().receive_json(content, **kwargs)

    async def chat_room_update(self, event):
        await self.send_json(content=event)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.model, self.channel_name)
        await self.close()

    async def dispatch_message(self, event):
        await self.send_json(content=event['data'])

class ChatConsumer(AsyncJsonWebsocketConsumer):
    '''this consumer handles specific room events'''
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
