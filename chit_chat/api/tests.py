from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from chat.models import Membership , Room

class AuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

    #sign up
    def test_existing_user_sign_up(self):

        response = self.client.post("/api/signup/", {
            "name": "testuser",
            "password": "password123"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_existing_user_sign_up(self):

        response = self.client.post("/api/signup/", {
            "name": "userNotExistingInDataBase",
            "password": "password234"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #login
    def test_login_user_not_found(self):
        response = self.client.post("/api/login/", {
            "name": "userNotExistingInDataBase",
            "password": "password234"
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_user_is_found_with_right_password(self):
        response = self.client.post("/api/login/", {
            "name": "testuser",
            "password": "password123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_is_found_with_wrong_password(self):
        response = self.client.post("/api/login/", {
            "name": "testuser",
            "password": "password234"
        })
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
    
    #logout
    def test_user_log_out_not_authenticated(self):
        response = self.client.get("/api/logout/", {
            "name": "testuser",
            "password": "password234"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_user_log_out_after_loging_in(self):
        # this cant actually happend because every use after login or sign up get login function auto.

        self.client.force_authenticate(user = self.user)
        response = self.client.get("/api/logout/", {
            "name": "testuser",
            "password": "password123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RoomTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = "testuser",
            password = "password123"
        )
        self.room = Room.objects.create(
            title = "test chat", 
            description = "this is test description",
        )
        self.client.force_authenticate(user = self.user)

    def test_invalid_url_response(self):
        membership = Membership.objects.create(user = self.user , room = self.room)
        response = self.client.get("/api/room/quit/ThisIsNotRealCode/")

        self.assertEqual(response.status_code , status.HTTP_404_NOT_FOUND)
    # joining is measured with existens of membership model instance.
    def test_user_without_not_joined(self):
        # no membership
        response = self.client.get(f"/api/room/quit/{self.room.code}/")
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)

    def test_user_is_joined_if_the_membership_is_deleted(self):
        
        membership = Membership.objects.create(user = self.user , room = self.room)
        response = self.client.get(f"/api/room/quit/{self.room.code}/")

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertFalse(
            Membership.objects.filter(room = self.room , user= self.user).exists()
        )
