from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LogoutApi,
    MembershipViewSet,
    RoomJoinApi,
    RoomViewSet,
    SignupApi,
    UserViewSet,
    LoginApi,
)

router = DefaultRouter()


router.register(r"rooms", RoomViewSet  ,basename = "room")
router.register(r"users", UserViewSet , basename="user")
router.register(r"memberships", MembershipViewSet , basename="membership")

urlpatterns = [

    path("login/" , LoginApi.as_view() , name = "loginApi"),
    path("room_join/<int:pk>/" , RoomJoinApi.as_view() , name = "roomJoinApi"),
    path("signup/" , SignupApi.as_view() , name = "signupApi"),
    path("logout/" , LogoutApi.as_view() , name = "logoutApi"),
    path("", include(router.urls)),
]
