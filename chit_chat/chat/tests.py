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

class InterconnectionChatSystem(TestCase):
    def setUp(self):
        user_one = User(username = "mike1" , password = "mike55555old1")
        user_two = User(username = "mike2" , password = "mike55555old2")
        user_three = User(username = "mike3" , password = "mike55555old3")

        user_one.save()
        user_two.save()
        user_three.save()

        
        room = Room(
            title = "cp programmers",
            description = "i like to be a very succesfull person", 
        )
        room.save()
        room.user.add(user_one , user_two , user_three)
        room.save()

        # i save 2 times because i overwrite the save method so changes the number_joined if not save it after the add ; number_joined would be 0

    def test_number_of_people_joined_on_room(self):
        room = Room.objects.get(title ="cp programmers")
        number = room.user.all().count()
        self.assertEqual(room.number_joined , number)


