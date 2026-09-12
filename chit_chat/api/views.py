from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from chat.models import Membership, Room  
from .serializer import (
    MembershipSerializer,
    RoomSerializer,
    UserSerializer,
)


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = RoomSerializer
    def get_queryset(self):
        user = self.request.user
        return user.room_set.all()

class RoomJoinApi(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request , pk):
        data = request.data
        room = Room.objects.filter(code = pk).first()

        if data['join']:
            Membership.objects.create(user = self.request.user , room = room)
            return Response({"message":"user was added"} , status=status.HTTP_200_OK)
        else:
            Membership.objects.filter(user = self.request.user , room__code = pk).delete()
            return Response({"message":"user was deleted"} , status=status.HTTP_200_OK)

class SignupApi(APIView):

    permission_classes = [AllowAny]
    def post(self , request):
        data = request.data
        try:
            user = User.objects.create_user(username = data['name'] , password= data['password'])
        except:
            return Response({"error":"problem in creating users"} , status=status.HTTP_400_BAD_REQUEST)
        login(request , user)
        return Response(status=status.HTTP_200_OK)



class LogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request):
        logout(request)

        return Response(status =status.HTTP_200_OK)

class LoginApi(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        data = request.data
        user = User.objects.filter(username = data['name']).first()

        if user is None :
            return Response({"error":"user was not found" } ,status =status.HTTP_404_NOT_FOUND)

        if user.check_password(data['password']):
            login(request , user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error":"the password is not right"} , status=status.HTTP_406_NOT_ACCEPTABLE)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer
    lookup_field = "room"

    def get_queryset(self):
        user = self.request.user
        return user.membership_set.all()

