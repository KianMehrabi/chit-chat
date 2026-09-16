from django.contrib.auth.forms import User
from django.test import TestCase
from rest_framework.views import status

from chat.models import Membership, Room

class RoomViewTest(TestCase):
    def setUp(self):
        user =  User.objects.create_user(username = "testuser" , password = "password123")
        self.client.force_login(user)
        self.user = user

        room = Room.objects.create(title = "chat" , description = "this is a chat room")
        self.room = room

        membership = Membership.objects.create(user = user , room = room)
        self.membership = membership

    def test_room_deleted_user_is_admin(self):
        self.membership.is_admin = True
        self.membership.save()

        response = self.client.get(f"/room/delete/{self.room.code}/")
        self.assertRedirects(response, "/")

        self.assertFalse(
        Room.objects.filter(code=self.room.code).exists()
        )

    def test_room_deleted_user_in_not_admin(self):
        self.membership.is_admin = False
        self.membership.save()

        response = self.client.get(f"/room/delete/{self.room.code}/")

        self.assertEqual(response.status_code , 401)

    def test_room_deleted_wrong_code(self):
        response = self.client.get("/room/delete/WrongCode/")

        self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)
