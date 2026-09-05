from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Profile, Room, Membership, Message, PhotoMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "password"]



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

