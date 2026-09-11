from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Profile, Room, Membership, Message, PhotoMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "password"]


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id' , 'title' , 'description']

