from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Profile, Room, Membership, Message, PhotoMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "password"]
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class PhotoMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoMessage
        fields = "__all__"
