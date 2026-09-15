from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LogoutApi,
    SignupApi,
    LoginApi,
    UserViewSet,
)

router = DefaultRouter()


router.register(r"users", UserViewSet , basename="user")

urlpatterns = [
    path("login/" , LoginApi.as_view() , name = "loginApi"),
    path("signup/" , SignupApi.as_view() , name = "signupApi"),
    path("logout/" , LogoutApi.as_view() , name = "logoutApi"),
    path("", include(router.urls)),
]
