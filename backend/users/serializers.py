from rest_framework import serializers
from .serializers import *
from .models import ImageModel, Profile

class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = ImageModel
        fields = ('name' ,'url')

    def get_url(self, image):
        request = self.context.get('request')
        photo_url = image.img.url
        return request.build_absolute_uri(photo_url)

    
class UserProfileSerializer(serializers.ModelSerializer):
    avatar = ImageSerializer(many=False, required=False)
    class Meta:
        model = Profile
        fields = [
            "avatar",
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