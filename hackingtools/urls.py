from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # GET http://127.0.0.1:8000/api/device/1/
    path("api/device/<int:pk>/", views.deviceView),
    # GET http://127.0.0.1:8000/api/devices/
    # POST http://127.0.0.1:8000/api/devices/
    path("api/devices/", views.deviceListView),
    # GET http://127.0.0.1:8000/api/devicelog/
    path("api/devicelog/<int:pk>/", views.deviceLogListView),
    path("api/devicelog/", views.deviceLogView),
]
