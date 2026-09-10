from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    RoomViewSet,
    UserViewSet,
    LoginApi,
)

router = DefaultRouter()


router.register(r"rooms", RoomViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("login/" , LoginApi.as_view() , name = "loginApi"),
    path("", include(router.urls)),
]
