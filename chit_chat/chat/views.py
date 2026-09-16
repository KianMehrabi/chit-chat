from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from rest_framework import status
from rest_framework.views import Response
from chat.models import Membership , Room
from chat.form import CodeForm, RoomForm

# i want a CBV because i can check if a method is POST or GET and not
# use if.
# i used CBV and clean_form logic. you can also do this with normal Api(with drf) or dont even error handle
class HomePage(View):
    def get(self , request):
        if not request.user.is_authenticated:
            return render(request , "chat/homepage.html")
        else:
            user = request.user
            memberships = user.membership_set.all()
            form = CodeForm()
            context = {
                "memberships":memberships,
                "form":form,
            }
            return render(request , "chat/authhomepage.html" , context)

    # the only form in my code is from CodeForm()
    def post(self, request):
        if request.user.is_authenticated:
            form = CodeForm(request.POST)
            user = request.user

            # this is where the logic of the code is checked so that the 
            # code is not joined before. check out room
            if form.is_valid():

                code = form.cleaned_data["code"]
                room = Room.objects.get(code = code)
                membership = Membership.objects.filter(user=user , room=room)
                if membership.exists():
                    messages.error(request , "You have that room already")
                    return redirect("homepage")
                else:
                    Membership.objects.create(user=user , room=room)
                    return redirect("homepage")
            else:
                    messages.error(request , form.errors["code"][0])
                    return redirect("homepage")
        else:
            return  HttpResponseBadRequest()




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

