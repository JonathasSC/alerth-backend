from django.urls import path
from .consumers import EventsConsumer

websocket_urlpatterns = [
    path('ws/', EventsConsumer.as_asgi()),
]
