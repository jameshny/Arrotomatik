import datetime

from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EarthHumidity(TimeStampMixin):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    humidity = models.FloatField()

class AirInformation(TimeStampMixin):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    temperature = models.FloatField()
    humidity    = models.FloatField()
