from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
]
