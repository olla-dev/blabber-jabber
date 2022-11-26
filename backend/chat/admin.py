from django.contrib import admin

from chat.models import ChatRoom, Message
from users.models import Profile

class ChatRoomAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Profile, ProfileAdmin)