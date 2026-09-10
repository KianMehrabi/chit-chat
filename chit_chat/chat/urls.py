from django.urls import path
from .views import home_page , login_page , sign_page

urlpatterns = [
    path("login/" , login_page,  name="login"),
    path("" , home_page,  name="homepage"),
    path("signup/" , sign_page,  name="signup"),
]
