from django.test import TestCase
from .models import Room, UserRoomCard
from django.contrib.auth.models import User

# Create your tests here.

class InterconnectionChatSystem(TestCase):
    def setUp(self):
        """
        mike0 and mike1 ==> roomA
        mike0, mike1 and mike2 ==> roomB
        mike1, mike2 ==> roomC

        and i am going to check the system
        """
        
        #creating some users for the interconnected system
        mike0 = User.objects.create(username="mike0" , password="mike55555old0")
        mike1 = User.objects.create(username="mike1" , password="mike55555old1")
        mike2 = User.objects.create(username="mike2" , password="mike55555old2")

        mike0.save()
        mike1.save()
        mike2.save()

        #creating the user-room-card
        mike0card = UserRoomCard.objects.create(created_by = mike0)
        mike1card = UserRoomCard.objects.create(created_by = mike1)
        mike2card = UserRoomCard.objects.create(created_by = mike2)


        mike0card.save()
        mike1card.save()
        mike2card.save()

        #now creating the room

        roomA= Room.objects.create()
        roomB = Room.objects.create()
        roomC = Room.objects.create()

        roomA.save()
        roomB.save()
        roomC.save()


        roomA.user.add(mike0card , mike1card)
        roomB.user.add(mike1card , mike1card,  mike2card)
        roomC.user.add(mike1card , mike2card)

    def test_just_to_see_the_setup(self):
        self.assertEqual(1,1)
