from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Room A'},
    {'id': 2, 'name': 'Room B'},
    {'id': 3, 'name': 'Room C'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, roomId):
    selectedRoom = None
    for room in rooms:
        if room['id'] == int(roomId):
            selectedRoom = room

    context = {'room': selectedRoom}
    return render(request, 'base/room.html', context)
