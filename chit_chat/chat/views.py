from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def home_page(request):
    return render(request , "chat/homepage.html")

def sign_page(self):
    return render(self , "chat/signup.html")

def login_page(self):
    return render(self , "chat/login.html")

def logout_page(request):
    if request.method == "POST":
        return redirect("homepage")

