'''
Created on 20/03/2015

@author: eoriol
'''

from rest_framework import serializers
from blog.models import Post, Comment, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'karma')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'owner')
        

class PostSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserProfile.objects.all(), source='owner')
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'ownerId', 'comments')

                


        