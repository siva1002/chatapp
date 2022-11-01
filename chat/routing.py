from django.urls import path , include
from chat.consumer import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
	path(r'ws/chatroom/<str:room>' , ChatConsumer.as_asgi()) 
]
