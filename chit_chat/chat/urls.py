from django.urls import path
from .views import home_page , login_page , sign_page , logout_page

urlpatterns = [
    path("" , home_page,  name="homepage"),
]
