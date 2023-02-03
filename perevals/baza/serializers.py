from .models import *
from rest_framework import serializers

class PhotoSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo', 'mpass__id', 'mpass__name']


class ZoneSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalZones
        fields = ['name']

class PassesSerial(serializers.HyperlinkedModelSerializer):
#    dbusers = DBUserSerial(many=True)
#    zones = ZoneSerial(many=True)

    class Meta:
        model = Passes
        fields = [
            'id',
            'name',
            'latitude',
            'latitude_zone',
            'longitude',
            'longitude_zone',
            'height',
            'winter_dif',
            'spring_dif',
            'summer_dif',
            'autumn_dif',
            'activ',
        ]

class DBUserSerial(serializers.HyperlinkedModelSerializer):
    dbusers = PassesSerial(many=True)
    class Meta:
        model = DBUser
        fields = ['name', 'email', 'phone', 'dbusers']

