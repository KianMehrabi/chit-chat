from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from chat.models import Room, Membership


class RoomViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.room = Room.objects.create(
            title="Test Room",
            description="Test description"
        )
        self.client.force_authenticate(user=self.user)

    def test_user_can_join_room(self):
        response = self.client.post(
            f"/api/room_join/{self.room.code}/",
            {"join": True},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "user was added")

    def test_user_can_un_join_room(self):

        response = self.client.post(
            f"/api/room_join/{self.room.code}/",
            {"join": False},
            format="json"
        )
        self.assertEqual(response.data["message"], "user was deleted")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_joining_makes_membership(self):
        response = self.client.post(
            f"/api/room_join/{self.room.code}/",
            {"join": True},
            format="json"
        )

        membership = Membership.objects.filter(user = self.user , room = self.room)
        self.assertTrue(membership.exists())
    def test_unjoining_makes_membership(self):
        response = self.client.post(
            f"/api/room_join/{self.room.code}/",
            {"join": False},
            format="json"
        )

        membership = Membership.objects.filter(user = self.user , room = self.room)
        self.assertFalse(membership.exists())
