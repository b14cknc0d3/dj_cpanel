from django.db import models
from rest_framework import serializers

from .models import DeviceID,Like,Comment,Share,News

class DeviceIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceID
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"
        
class ShareSerializer(serializers.ModelSerializer):
    # device_id = DeviceIDSerializer()
    class Meta:
        model = Share
        fields = "__all__"
        
        
class NewsSerializer(serializers.ModelSerializer):
    
    # like = LikeSerializer()
    # comment = CommentSerializer()
    # share = ShareSerializer()
    like = serializers.ReadOnlyField(source="like_count")
    comment = serializers.ReadOnlyField(source="comment_count")
    share = serializers.ReadOnlyField(source="share_count")
    class Meta:
        model = News
        fields = ("id","news_image","news_title","news_body","created_at", "updated_at","like","comment","share")
