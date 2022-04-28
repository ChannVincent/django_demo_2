from django.contrib.auth.models import User, Group
from hackingtools.models import Device, DeviceLog
from rest_framework import viewsets
from rest_framework import permissions
from hackingtools.serializers import (
    DeviceSerializer,
)
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


@csrf_exempt
def deviceView(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = DeviceSerializer(device)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(device, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        device.delete()
        return HttpResponse(status=204)


@csrf_exempt
def deviceListView(request):
    if request.method == "GET":
        snippets = Device.objects.all()
        serializer = DeviceSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
