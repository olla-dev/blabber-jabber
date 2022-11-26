from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import *
from .models import Profile
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "bio",
            "age",
            "is_verified",
            "is_banned",
            "is_premium",
            "social_facebook",
            "social_instagram",
            "social_youtube",
            "social_blog",
        ]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'profile', 
            'username', 
            'first_name',
            'last_name',
            'email'
        )