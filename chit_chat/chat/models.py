from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length = 50 , blank = True)
    age = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
        blank = True
    )
    phone = models.IntegerField(blank = True)
    show_phone = models.BooleanField(default=True , blank = True)
    living_place = models.CharField(max_length = 50, blank= True)
    bio = models.TextField(max_length = 250 , blank = True)



class Room(models.Model):
    title = models.TextField(max_length = 26 , default = "chat")
    user = models.ManyToManyField(User , through="Membership")
    description = models.TextField(max_length = 250 , default = "")

    def __str__(self):
        return f'|{self.id}|'

    def save(self , *args , **kwargs):
        if self.id != None:
            self.number_joined = self.user.all().count()
        else:
            pass
        super(Room , self).save(*args , **kwargs)

class Membership(models.Model):
    room = models.ForeignKey(Room , on_delete=models.CASCADE , null =True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null = True , related_name="user")

    is_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_muted = models.BooleanField(default=False)
    joined_at = models.DateTimeField(null = True)

    def __str__(self):
        return f'|{self.user.username}|{self.room.id}|'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["room" , "user"], name = "unique_room_user"
            )
        ]

class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , null = True)
    profile = models.ForeignKey(Profile ,on_delete=models.CASCADE , null= True)
    content = models.TextField(max_length = 150)
    is_sent = models.BooleanField(default=True)
    is_seen = models.BooleanField(default=False)
    is_changed = models.BooleanField(default=False)

    def __str__(self):
        return  f'|{self.user}|{self.room}'

    class Meta:
        verbose_name = "Message"
        ordering = ["created_at"]


class PhotoMessage(Message):
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
