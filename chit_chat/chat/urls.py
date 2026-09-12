from django.urls import path
from .views import home_page , login_page , sign_page , room_detail_page

urlpatterns = [
    path("login/" , login_page,  name="login"),
    path("" , home_page,  name="homepage"),
    path("signup/" , sign_page,  name="signup"),
    path("room/<int:pk>/" , room_detail_page , name= "room-detail-page")
]
