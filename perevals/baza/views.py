from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
import json

from .models import *
from .serializers import *

class PassesViewset(viewsets.ModelViewSet):
    queryset = Passes.objects.all()
    serializer_class = PassesSerial

class PhotoViewset(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerial

def submitData(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            if DBUser.objects.filter(email=req['email']).exists():
                user = DBUser.objects.get(email=req['email'])
                user.name = req['username']
                user.phone = req['phone']
                user.save()
            else:
                user = DBUser.objects.create(
                    name=req['username'],
                    email=req['email'],
                    phone=req['phone'],
                )
            new = Passes.objects.create(
                name=req['title'],
                latitude=req['latitude'],
                latitde_zone=req['latitude_zone'],
                longitude=req['longitude'],
                longitude_zone=req['longitude_zone'],
                height=req['height'],
                by_user=user,
                winter_dif=req['winter_dif'],
                spring_dif=req['spring_dif'],
                summer_dif=req['summer_dif'],
                autumn_dif=req['autumn_dif'],
            )
            if not (req['photos'] == None or req['photos'] == []):
                for i in req['photos']:
                    Photo.objects.create(photo=i, mpass=new)
            return HttpResponse(json.dumps({
                "status": 200,
                "message": None,
                "id": new.id,
            }))
        except:
            return HttpResponse(json.dumps({
                "status": 400,
                "message": "Wrong fields",
                "id": None,
            }))
    else:
        return HttpResponse(json.dumps({
            "status": 500,
            "message": "Wrong request",
            "id": None,
        }))
