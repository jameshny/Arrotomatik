import traceback
from .models import EarthHumidity, AirInformation
from .serializers import EarthHumiditySerializer, AirInformationSerializer
from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.exceptions import ParseError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import OAuth2Authentication


class EarthHumidityList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EarthHumiditySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = EarthHumidity.objects.filter(user=self.request.user)
        return queryset


class AirInformationList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AirInformationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = AirInformation.objects.filter(user=self.request.user)
        return queryset