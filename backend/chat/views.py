from .pagination import ResultPagination
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework import viewsets, generics, status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import Http404
from django.core.cache import cache
from django.db.models import Q
from .models import Message

from core.settings import CACHE_TTL

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MessageView(viewsets.ReadOnlyModelViewSet):
    '''This ViewSet serves all messages info'''
    model = Message
    serializer_class = MessageSerializer
    lookup_field='id'
    # Optimization: 
    # I should use a cursor pagination if a vessel has a huge list of locations.
    # will try to do it, if I finish the UI :/
    queryset = Message.objects.prefetch_related('author').all()
