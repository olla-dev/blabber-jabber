from django.urls import re_path
from .consumers import ChatConsumer, ChatEventConsumer

websocket_urlpatterns = [
    re_path(r'ws/lobby/', ChatEventConsumer.as_asgi()),
    re_path(r"ws/room/(?P<room_name>\w+)/$", ChatConsumer.as_asgi())
]