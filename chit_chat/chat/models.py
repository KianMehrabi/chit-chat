from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserRoomCard(models.Model):
    joined_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User , on_delete=models.CASCADE)
    is_muted = models.BooleanField(default=False)

class Room(models.Model):
    user = models.ManyToManyField(UserRoomCard)

class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , null=True)
    created_by = models.ForeignKey(User ,on_delete=models.CASCADE)
    content = models.TextField(max_length = 150)
    is_seen = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Message"
        ordering = ["created_at"]

