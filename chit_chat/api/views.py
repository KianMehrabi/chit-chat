from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets 
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
from chat.models import Room  
from .serializer import (
    RoomSerializer,
    UserSerializer,
)

"""

the reason the login in works: request is just an Attribute of the instance class of UserViewSet and its same as django normal request
so i can access it from self , it beautiful and saves a full search of DB

"""

class LoginApi(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        data = request.data
        user = get_object_or_404(User , password= data['password'])
        if user.username == data['name']:
            login(request , user)
            return Response(status=200)
        else:
            return Response({"error":"user name is not correct"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        print(user.password)
        created_user = authenticate(self.request , username = user.username , password = user.password)
        login(self.request, user)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

