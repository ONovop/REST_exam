from .models import *
from rest_framework import serializers

class PhotoSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']


class ZoneSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalZones
        fields = ['name']

class DBUserSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBUser
        fields = ['name', 'email', 'phone']

class PassesSerial(serializers.HyperlinkedModelSerializer):
    dbusers = DBUserSerial(many=False, source='by_user')
    zones = ZoneSerial(many=False, source='zone')
    photos = PhotoSerial(many=True)

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
            'dbusers',
            'zones',
            'photos',
        ]



