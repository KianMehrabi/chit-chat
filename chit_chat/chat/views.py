from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.views import Response
from chat.models import Membership , Room
from chat.form import RoomForm

def home_page(request):
    if not request.user.is_authenticated:
        return render(request , "chat/homepage.html")
    else:
        user = request.user
        memberships = user.membership_set.all()
        context = {
            "memberships":memberships,
        }
        return render(request , "chat/authhomepage.html" , context)

@login_required
def room_page(request , pk):
    room = get_object_or_404(Room , code=pk)
    context = {
        "room":room
    }
    return render(request , "chat/room.html" , context)

@login_required
def delete_room(request , pk):
    user = request.user
    room = get_object_or_404(Room , code = pk)
    membership = room.membership_set.get(user = user)
    if not membership.is_admin:
        return HttpResponse("permission deinied" , status = 401)

    room.delete()
    return redirect("homepage")

def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form = form.save()
            Membership.objects.create(user = request.user , room = form , is_admin = True)
            return redirect("homepage")

    else:
        form = RoomForm()
    context = {
        "form": form
    }
    return render(request , "chat/createroom.html" , context)

def update_room(request , pk):
    instance = get_object_or_404(Room, code=pk)
    form = RoomForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'chat/updateroom.html', {'form': form}) 

def sign_page(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403)
    return render(request , "chat/signup.html")

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403)
    return render(request , "chat/login.html")

