
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.shortcuts import render, redirect
from .form import *
from django.http import HttpResponse
from .form import *
def signin(request):
    form = loginform()
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email,password=password)
        print(email)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('room')
    return render(request, 'chat/loginpage.html', {'form': form})


def chatPage(request, name, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    return render(request, "chat/chatpage.html",{'roomname':name})


def roomname(request):
    form = room()
    return render(request, 'chat/room.html', {'form': form})
# async def index(request):
#     return HttpResponse("Hello, async Django!")
def signup(request):
    form=signupform()
    if request.method=='POST':
      form=  signupform(request.POST)
      if form.is_valid():
        form.save()
        return redirect('login-user')
      else:
        print(form.errors)
    return render(request,'chat/signupform.html',{'form':form})