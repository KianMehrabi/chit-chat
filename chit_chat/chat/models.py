from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    name = models.TextField(max_length = 26 , default = "chat")
    user = models.ManyToManyField(User , through="Membership")

class Membership(models.Model):
    room = models.ForeignKey(Room , on_delete=models.CASCADE , null =True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_muted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["room" , "user"], name = "unique_room_user"
            )
        ]

class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , null = True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE , null = True)
    content = models.TextField(max_length = 150)
    is_seen = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Message"
        ordering = ["created_at"]

