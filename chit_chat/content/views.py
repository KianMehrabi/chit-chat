from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from chat.models import Room
from django.contrib.auth import logout , login , authenticate

# Create your views here.

def home_page(request):
    rooms = Room.objects.filter(user__username = request.user.username )
    return render(request , "content/homepage.html" )

def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("homepage")

def sign_up(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return HttpResponse("existing user in DB")

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect("homepage")
    elif request.method == "GET":
        return render(request , "content/signup.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponse("no user with the info in DB")

        return redirect("homepage")
    elif request.method == "GET":
        return render(request , "content/login.html")

