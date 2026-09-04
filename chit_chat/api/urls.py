from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProfileViewSet,
    RoomViewSet,
    MembershipViewSet,
    MessageViewSet,
    PhotoMessageViewSet,
)

router = DefaultRouter()

router.register(r"profiles", ProfileViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"memberships", MembershipViewSet)
router.register(r"messages", MessageViewSet)
router.register(r"photo-messages", PhotoMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
