from django.urls import path
from .views import home_page , login_page , sign_page , logout_page

urlpatterns = [
    path("" , home_page,  name="homepage"),
    path("signup/" , sign_page,  name="signup"),

    path("login/" , login_page,  name="login"),
    path("logout/" , logout_page,  name="logout"),
]
