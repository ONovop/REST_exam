from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *

class PassesViewset(viewsets.ModelViewSet):
    queryset = DBUser.objects.all()
    serializer_class = DBUserSerial

class PhotoViewset(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerial
