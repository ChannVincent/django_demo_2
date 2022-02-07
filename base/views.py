from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


def home(request):
    rooms = Room.objects.all()  # database query
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, roomId):
    selectedRoom = None
    selectedRoom = Room.objects.get(id=roomId)  # database query
    context = {"room": selectedRoom}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)
