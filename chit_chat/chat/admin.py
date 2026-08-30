from django.contrib import admin
from .models import Room, Message , UserRoomCard

# Register your models here.

admin.site.register([Room, Message , UserRoomCard])
