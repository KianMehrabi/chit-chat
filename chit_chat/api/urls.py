from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    RoomViewSet,
    UserViewSet,
)

router = DefaultRouter()


router.register(r"rooms", RoomViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
