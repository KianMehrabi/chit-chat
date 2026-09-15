from django.urls import path
from .consumers import HahahaConsumer

websocket_urlpatterns = [
    path("ws/chat/", HahahaConsumer.as_asgi()),
]
