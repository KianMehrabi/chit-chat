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

    def test_membership_existed_before_creating(self):
        Membership.objects.create(user = self.user , room = self.room)

        response = self.client.post(
            f"/api/room_join/{self.room.code}/",
            {"join": True},
            format="json"
        )

        self.assertEqual(response.status_code , 400)

    # this will never happend because the url will be invalid and django gives a 404 by itself
    # django 404 give a html response but drf reponse( in here mine) will give json so be cureful in the frontend

    # i kept this one because it isnt a bad practice to have edge cases
    def test_invalid_room_tags(self):
        response = self.client.post(
            f"/api/room_join/BS/",
            {"join": True},
            format="json"
        )

        self.assertEqual(response.status_code , 404)

