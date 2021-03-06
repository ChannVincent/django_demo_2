from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:roomId>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:roomId>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:roomId>/", views.deleteRoom, name="delete-room"),
]
