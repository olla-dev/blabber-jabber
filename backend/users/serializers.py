from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import *
from .models import Profile
from django.contrib.auth.models import User
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "bio",
            "age",
            "online",
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

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password'
        )

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
    
    def create(self, validated_data):
        """Create and return a new user."""

        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user