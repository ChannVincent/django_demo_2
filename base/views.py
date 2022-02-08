from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm


def home(request):

    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)  # = topic.name.contains(q) case insensitive
        | Q(name__icontains=q)
        | Q(host__username__icontains=q)
    )
    topics = Topic.objects.all()  # database query
    context = {"rooms": rooms, "topics": topics}
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


def updateRoom(request, roomId):
    room = Room.objects.get(id=roomId)
    form = RoomForm(instance=room)  # prefill form with room attributes
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)  # save over room instance
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, roomId):
    room = Room.objects.get(id=roomId)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})
