from rest_framework import serializers
from group.models import Group
from user.models import User,Comment,Post
from .models import TestModel

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model= Group
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email','age','profile_pic','name','groups']

class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model= Comment
        fields=['user','comment']

class PostSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model= Post
        fields='__all__'

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestModel
        fields='__all__'