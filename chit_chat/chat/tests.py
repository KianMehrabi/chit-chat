from django.db.models import QuerySet
from django.test import TestCase
from .models import Profile, Room, Membership
from django.contrib.auth.models import User

# Create your tests here.
"""

    def setUp(self):
        user_one = User.objects.create(username= "mike_one" , password = "mike_admin_500")
        user_one.save()

        room_one = Room.objects.create(name="chat to nothing")
        room_one.save()

        membership_one = Membership.objects.create(
            user = user_one,
            room = room_one
        )
        membership_one.save()

    def test_does_the_room_have_name(self):
        # for now if this fails the membership test will fail too be curefull

        user_one = User.objects.get(username= "mike_one")
        room_one = Room.objects.filter(user= user_one).first()

        self.assertEqual(room_one.name , "chat to nothing")

    def test_membership(self):
        # fix later
        # so basicly i dont have any usefull info so for now i am testing the membership by the room its realated to not good practice but works for now

        created_user = User.objects.filter(username = "mike_one").first()
        membership = Membership.objects.filter(user = created_user).first()
        self.assertEqual(membership.room.name , "chat to nothing")

    def test_user_is_real_or_not(self):
        #checking with the password becouse its more safe
        
        created_user  = User.objects.filter(username= "mike_one").first()
        self.assertEqual(created_user.password , "mike_admin_500")
"""

class RoomModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1" , password="password134")
        self.room = Room.objects.create(title="chat one" , description="this is chat one")

    def test_membership_from_user(self):
        membership = Membership.objects.create(user= self.user , room= self.room)
        user_membership = self.user.membership_set.filter(room = self.room)
        self.assertEqual(user_membership.exists() , True )

    def test_membership_from_room(self):
        membership = Membership.objects.create(user= self.user , room= self.room)
        room_membership = self.room.membership_set.filter(user = self.user)
        self.assertEqual(room_membership.exists() , True )

    def test_room_user_existing_after_creating_membership(self):
        membership = Membership.objects.create(user= self.user , room= self.room)
        user_in_room = self.room.user.all().first()
        self.assertEqual(user_in_room.username , self.user.username)
