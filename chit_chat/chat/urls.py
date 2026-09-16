from django.urls import path
from .views import home_page , login_page, room_page , sign_page , delete_room , create_room , update_room

urlpatterns = [
    path("login/" , login_page,  name="login"),
    path("room/delete/<str:pk>/" , delete_room , name="deleteRoom"),
    path("room/update/<str:pk>/" , update_room , name="updateRoom"),
    path("room/create/" , create_room , name="createRoom"),
    path("room/<str:pk>/" , room_page,  name="room"),
    path("" , home_page,  name="homepage"),
    path("signup/" , sign_page,  name="signup"),
]
