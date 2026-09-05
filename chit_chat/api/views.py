from django.shortcuts import redirect
from rest_framework import viewsets , permissions
from django.contrib.auth.models import User
from rest_framework.views import Response
from chat.models import Profile, Room, Membership, Message, PhotoMessage
from .serializer import (
    ProfileSerializer,
    UserSerializer,
    RoomSerializer,
    MembershipSerializer, 
    MessageSerializer,
    PhotoMessageSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ permissions.AllowAny]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class PhotoMessageViewSet(viewsets.ModelViewSet):
    queryset = PhotoMessage.objects.all()
    serializer_class = PhotoMessageSerializer




