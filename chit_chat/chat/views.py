from django.contrib.auth.views import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def home_page(request):
    print(request.user)
    if not request.user.is_authenticated:
        return render(request , "chat/homepage.html")
    else:
        return render(request , "chat/authhomepage.html")

def sign_page(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403)
    return render(request , "chat/signup.html")

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403)
    return render(request , "chat/login.html")

