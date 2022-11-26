from .pagination import ResultPagination
from rest_framework.response import Response
from .serializers import MessageSerializer, ChatRoomSerializer
from rest_framework import viewsets, generics, status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import Http404
from django.core.cache import cache
from django.db.models import Q
from .models import Message, ChatRoom

from core.settings import CACHE_TTL

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MessageView(viewsets.ReadOnlyModelViewSet):
    '''This ViewSet serves all messages info accross all channels'''
    model = Message
    serializer_class = MessageSerializer
    lookup_field='id'
    queryset = Message.objects.prefetch_related('author').all()

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class RoomListView(viewsets.ReadOnlyModelViewSet):
    '''This ViewSet serves all messages info'''
    model = ChatRoom
    serializer_class = ChatRoomSerializer
    lookup_field='id'
    queryset = ChatRoom.objects.prefetch_related('users').all()

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class RoomMessageListView(viewsets.ModelViewSet):
    '''This ViewSet serves a room's latest 10 messages'''
    model = Message
    serializer_class = MessageSerializer
    pagination_class = ResultPagination

    def get_queryset(self):
        # get room id from url
        room_id = self.kwargs['room_id']
        
        # check for query filter
        filter = self.request.query_params.get('filter')
        if filter is not None:
            filtered_messages = Message.objects.filter(
                Q(content__icontains = filter)
            )
            cached_messages = filtered_messages
            cache.set(f"room_{room_id}_messages", cached_messages, CACHE_TTL)
            return cached_messages
        else:
            cached_messages = cache.get(f"room_{room_id}_messages")
            if not cached_messages:
                cached_messages = Message.objects.filter(room__id=room_id).order_by('-sent_time_utc')
                cache.set(f"room_{room_id}_messages", cached_messages, CACHE_TTL)
        
        return cached_messages

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class RoomDetailView(viewsets.ModelViewSet):
    """
    Retrieve, update or delete a chat room instance.
    """
    serializer_class = ChatRoomSerializer
    pagination_class = ResultPagination

    def get_queryset(self):
        # here drf-nested-router appends parent name to the query param, hence use vessel_vessel_id below
        room_id = self.kwargs['pk']
        return ChatRoom.objects.prefetch_related('users').filter(id=room_id)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            room_id = self.kwargs['pk']

            if ChatRoom.objects.filter(id=room_id).exists():
                instance = ChatRoom.objects.get(id=room_id)
                instance.delete()
                cache.remove(f"room_{room_id}_messages")
            else: 
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
        

