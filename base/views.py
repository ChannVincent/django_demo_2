from django.shortcuts import render
from .models import Room



def home(request):
    rooms = Room.objects.all() # database query
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, roomId):
    selectedRoom = None
    selectedRoom = Room.objects.get(id=roomId) # database query
    context = {'room': selectedRoom}
    return render(request, 'base/room.html', context)
