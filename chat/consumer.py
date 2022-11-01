import imp
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import authenticate, login
from channels.db import database_sync_to_async
from .form import *
from django.shortcuts import render, redirect
import channels
class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = []

    async def connect(self):
        self.room = self.scope['url_route']['kwargs']['room']
        #self.user.append(self.scope['url_route']['kwargs']['int'])
        self.roomGroupName = 'chatroom-%s' % self.room
        user=await channels.auth.get_user(self.scope)
        self.user.append(user.id)
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        print(self.user)
        print(self.scope)
       # print(self.channel_name,' created channel-name',self.channel_layer,'channel-layer created')
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        print(text_data_json)
        # await login(self.scope, user)
        #save the session (if the session backend does not access the db you can use `sync_to_async`)
        #await database_sync_to_async(self.scope["session"].save)()
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            })

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))
async def signin(request):
    form = loginform()
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(email)
        print(user)
        if user is not None:
            await login(request, user)
            return redirect('room')
    return render(request, 'chat/loginpage.html', {'form': form})
