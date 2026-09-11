from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets 
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from chat.models import Room  
from .serializer import (
    RoomSerializer,
    UserSerializer,
)

"""
the reason the logic works: request is just an Attribute of the instance class of UserViewSet and its same as django normal request
so i can access it from self , it beautiful and saves a full search of DB
"""

class SignupApi(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        try:
            is_user = User.objects.filter(password = request.data['password'])
            if len(is_user) > 1:
                return Response({"error":"there many users with the same name"} , status = status.HTTP_400_BAD_REQUEST)
            user = User(username = request.data['name'], password = request.data['password'])
            user.save()
            login(request, user)
            return Response(status = status.HTTP_200_OK)
        except:
            return Response({"error":"cant create user because user was created before"} ,status=status.HTTP_400_BAD_REQUEST)


class LogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request):
        logout(request)

        return Response(status =status.HTTP_200_OK)

class LoginApi(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        data = request.data
        user = User.objects.filter(username = data['name'])

        if len(user) > 1:
            return Response({"error":"there is more than one user with one password"}, status=status.HTTP_400_BAD_REQUEST)
        elif user is None:
            return Response({"error":"user was not found" } ,status =status.HTTP_404_NOT_FOUND)


        if user.first().password != data['password']:
            return Response({"error":"password didnt match" } ,status =status.HTTP_400_BAD_REQUEST)
        else:
            login(request , user.first())
            return Response(status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        created_user = authenticate(self.request , username = user.username , password = user.password)
        login(self.request, user)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

