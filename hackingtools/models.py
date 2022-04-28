from django.db import models


class Device(models.Model):
    serial_id = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    software = models.CharField(max_length=200)


class DeviceLog(models.Model):
    device = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, related_name="logs"
    )
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
