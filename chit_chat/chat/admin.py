from django.contrib import admin
from .models import Room, Message , Membership

# Register your models here.

admin.site.register([Message , Membership])

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
