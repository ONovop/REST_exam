from .models import *
from rest_framework import serializers

class PassesSerial(serializers.HyperlinkedModelSerializer):
    model = Passes
    fields = [
        'id',
        'name',
        'latitude',
        'latitude_zone',
        'longitude',
        'longitude_zone',
        'height',
        'by_user__name',
        'by_user__email',
        'by_user__phone',
        'zone__name',
        'winter_dif',
        'spring_dif',
        'summer_dif',
        'autumn_dif',
        'activ',
    ]

class PhotoSerial(serializers.HyperlinkedModelSerializer):
    model = Photo
    fields = ['photo', 'mpass__id', 'mpass__name']
