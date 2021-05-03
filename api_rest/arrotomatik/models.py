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
    date     = models.DateField(auto_now=True)
    humidity = models.DecimalField(max_digits=4, decimal_places=2)

class AirInformation(TimeStampMixin):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date        = models.DateField(auto_now=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    humidity    = models.DecimalField(max_digits=4, decimal_places=2)
