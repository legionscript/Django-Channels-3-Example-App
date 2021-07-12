from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns = [
	path('ws/counter/', WSConsumer.as_asgi()),
]