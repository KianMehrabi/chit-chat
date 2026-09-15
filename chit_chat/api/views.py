from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from chat.models import Membership, Room  
from .serializer import (
    UserSerializer,
)


# Auth
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
        user = User.objects.filter(username = data['name'])
        command = len(user)

        match command:
            case 1:
                user = user.first()
                if user.check_password(data['password']):
                    login(request , user)
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({"error":"the password is not right"} , status=status.HTTP_406_NOT_ACCEPTABLE)
            case 0:
                return Response({"error":"user was not found" } ,status =status.HTTP_404_NOT_FOUND)
            case _:
                return Response({"error":"there is problems with this user"} , status=status.HTTP_300_MULTIPLE_CHOICES)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

