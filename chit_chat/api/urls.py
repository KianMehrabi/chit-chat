from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LogoutApi,
    RoomViewSet,
    SignupApi,
    UserViewSet,
    LoginApi,
)

router = DefaultRouter()


router.register(r"rooms", RoomViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("login/" , LoginApi.as_view() , name = "loginApi"),
    path("signup/" , SignupApi.as_view() , name = "signupApi"),
    path("logout/" , LogoutApi.as_view() , name = "logoutApi"),
    path("", include(router.urls)),
]
