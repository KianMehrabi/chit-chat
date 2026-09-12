from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from chat.models import Room , Membership


class RoomViewSetTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )


        self.room = Room.objects.create(
            title="Test Room",
            description="Test description"
        )


        self.client.force_authenticate(user=self.user)

    def test_partial_update(self):
        response = self.client.patch(
            f"/api/rooms/{self.room.id}/",
            {"join":True}, 
            format="json",
        )

        print(response)

        room_test = self.user.membership_set.filter(room__id = self.room.id)

        self.assertEqual(room_test.exists(),  True)
