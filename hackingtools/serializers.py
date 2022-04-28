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
    # device = serializers.CharField(source="device.serial_id", read_only=True)

    def create(self, validated_data):
        return DeviceLog.objects.create(**validated_data)
