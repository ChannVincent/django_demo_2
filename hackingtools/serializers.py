from django.contrib.auth.models import User, Group
from hackingtools.models import Device, DeviceLog
from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    serial_id = serializers.CharField(required=True, allow_blank=True, max_length=200)
    model = serializers.CharField(required=False, allow_blank=True, max_length=200)
    software = serializers.CharField(required=False, allow_blank=True, max_length=200)

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.serial_id = validated_data.get("serial_id", instance.serial_id)
        instance.model = validated_data.get("model", instance.model)
        instance.software = validated_data.get("software", instance.software)
        instance.save()
        return instance


class DeviceLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    latitude = serializers.CharField(required=False, allow_blank=True, max_length=200)
    longitude = serializers.CharField(required=False, allow_blank=True, max_length=200)
    serial_id = serializers.CharField(required=False, allow_blank=True, max_length=200)
    model = serializers.CharField(required=False, allow_blank=True, max_length=200)
    software = serializers.CharField(required=False, allow_blank=True, max_length=200)

    def create(self, validated_data):
        serial_id = validated_data.get("serial_id")
        if serial_id == None:
            return None

        device = None
        try:
            device = Device.objects.get(serial_id=serial_id)
        except Device.DoesNotExist:
            device = Device()
            device.serial_id = serial_id
            device.model = validated_data.get("model", device.model)
            device.software = validated_data.get("software", device.software)
            device.save()

        deviceLog = DeviceLog()
        deviceLog.device = device
        deviceLog.latitude = validated_data.get("latitude")
        deviceLog.longitude = validated_data.get("longitude")
        deviceLog.save()
        return deviceLog
