from django.contrib import admin
from .models import Room, Message , Membership

# Register your models here.

admin.site.register([Room, Message , Membership])
