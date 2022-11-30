import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from datetime import datetime
from channels.db import database_sync_to_async
from chat.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer, MessageSerializer
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

        print("Connected to main channel!")
        await self.send_json(
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
            await self.send_json({
                "result": -1,
                "reason": "No command"
            })
        if not user_id:
            await self.send_json({
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

    async def user_status_update(self, event):
        '''Sends updates when a user logs in or logs out'''
        await self.send_json(content=event)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.model, self.channel_name)
        await self.close()

    async def dispatch_message(self, event):
        await self.send_json(content=event['data'])

class ChatConsumer(AsyncJsonWebsocketConsumer):
    '''this consumer handles specific room events'''
    
    @database_sync_to_async
    def save_message(self, user_id, message): 
        room = ChatRoom.objects.filter(name=self.room_name).first()
        user = User.objects.filter(id=user_id).first()
        if user in room.users:
            message = Message()
            message.author = user
            message.content = message
            message.room = room
            message.sent_time_utc = datetime.now()
            message.save()
            message_json = MessageSerializer(message, many=False).data
            return message_json
        else: 
            return None

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        await self.accept()

        print(f"Connected to room {self.room_name}!")
        self.send_json(
            {
                "type": "welcome_message",
                "message": f"Hey there! welcome to {self.room_name}",
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.model, self.channel_name)
        await self.close()

    async def dispatch_message(self, event):
        await self.send_json(content=event['data'])

    async def receive_json(self, content, **kwargs):
        command = content["command"]
        user_id = content["user"]

        if not command: 
            await self.send_json({
                "result": -1,
                "reason": "No command"
            })

        elif not user_id:
            await self.send_json({
                "result": -1,
                "reason": "No user provided"
            })
        else:
            # handle command
            if command == "message":
                message = content["message"]

                # save message to db
                saved_message = await self.save_message(user_id, message)
                
                if saved_message:
                    # Send message to room group
                    await self.channel_layer.group_send(
                        self.room_group_name, {"type": "new_message", "message": saved_message}
                    )
                else: 
                    await self.send_json({
                        "result": -1,
                        "reason": "User is not member of this chat room"
                    })

            if command == "typing":
                # user joins the chat room
                user_id = content["user"]
                
                await self.channel_layer.group_send(
                    self.room_group_name, {"type": "user_typing", "user_id": user_id}
                )

        return super().receive_json(content, **kwargs)

    async def user_typing(self, event):
        '''Sends updates when a user is typing'''
        await self.send_json(content=event)

    # Receive message from room group
    async def new_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
