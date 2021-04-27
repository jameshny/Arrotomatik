from rest_framework import serializers
from .models import EarthHumidity, AirInformation
import logging

logger = logging.getLogger(__name__)

class EarthHumiditySerializer(serializers.ModelSerializer):

    class Meta:
        model = EarthHumidity
        exclude = ['created_at', 'updated_at', 'user']

class AirInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirInformation
        exclude = ['created_at', 'updated_at', 'user']