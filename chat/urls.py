from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
	path("<str:name>/", chatPage, name="chat-page"),
	path("accounts/roomcall/", roomname, name="room"),
	# login-section
	path("accounts/login/",signin,name="login-user"),
	path("logout/", LogoutView.as_view(), name="logout-user"),
	path('',signup)
]