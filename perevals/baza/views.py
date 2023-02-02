from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *

class PassesViewset(viewsets.ModelViewSet):
    queryset = Passes.objects.all()
    serializer_class = PassesSerial

class PhotoViewset(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerial
