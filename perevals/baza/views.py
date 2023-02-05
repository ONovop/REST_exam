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
                latitude_zone=req['latitude_zone'],
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

def get_patch(request, **kwargs):
    obj_id = kwargs.get('pk')
    if not Passes.objects.filter(id=obj_id).exists():
        return HttpResponse(json.dumps({
            "status": 404,
            "message": "Such id doesn't exist",
            "id": obj_id,
        }))
    obj = Passes.objects.get(id=obj_id)
    if request.method == 'GET':
        photos = []
        if Photo.objects.filter(mpass__id=obj_id).exists():
            photos_qs = Photo.objects.filter(mpass__id=obj_id)
            for i in photos_qs:
                photos.append(i.photo)
        return HttpResponse(json.dumps({
            "id": obj.id,
            "title": obj.name,
            "latitude": obj.latitude,
            "latitude_zone": obj.latitude_zone,
            "longitude": obj.longitude,
            "longitude_zone": obj.longitude_zone,
            "height": obj.height,
            "winter_dif": obj.winter_dif,
            "spring_dif": obj.spring_dif,
            "summer_dif": obj.summer_dif,
            "autumn_dif": obj.autumn_dif,
            "activities": obj.activ,
            "zone": obj.zone.name,
            "g_zone": obj.zone.global_zone.name,
            "status": obj.status,
            "username": obj.by_user.name,
            "email": obj.by_user.email,
            "phone": obj.by_user.phone,
            "photos": photos,
        }))
    elif request.method == 'PATCH':
        if obj.status != 'N':
            return HttpResponse(json.dumps({
                "state": 0,
                "message": "Object is taken for moderation, editing is prohibited",
                "is": obj_id,
            }))
        try:
            req = request.body
            obj.name = req['title']
            obj.latitude = req['latitude']
            obj.latitude_zone = req['latitude_zone']
            obj.longitude = req['longitude']
            obj.longitude_zone = req['longitude_zone']
            obj.height = req['height']
            obj.winter_dif = req['winter_dif']
            obj.spring_dif = req['spring_dif']
            obj.summer_dif = req['summer_dif']
            obj.autumn_dif = req['autumn_dif']
            obj.save()
            baza = []
            baza_id = []
            if Photo.objects.filter(mpass__id=obj_id).exists():
                for i in Photo.objects.filter(mpass__id=obj_id):
                    baza.append(i.photo)
                    baza.append(i.id)
            if not (req['photos'] == None or req['photos'] == []):
                for i in req['photos']:
                    if i not in baza:
                        Photo.objects.create(photo=i, mpass=obj_id)
                for i in range(len(baza)):
                    if baza[i] not in req['photos']:
                        Photo.objects.get(id=baza_id[i]).delete()
            return HttpResponse(json.dumps({
                "state": 1,
                "message": None,
                id: obj_id,
            }))
        except:
            return HttpResponse(json.dumps({
                "state": 0,
                "message": "Wrong fields",
                "id": None,
            }))
    else:
        return HttpResponse(json.dumps({
            "status": 500,
            "message": "Wrong request",
            "id": None,
        }))

def user_filter(request, **kwargs):
    us_email = kwargs.get('email')
    if not DBUser.objects.filter(email=us_email).exists():
        return HttpResponse(json.dumps({
            "status": 404,
            "message": "Such user doesn't exist",
            "email": us_email,
        }))
    if request.method != 'GET':
        return HttpResponse(json.dumps({
            "status": 500,
            "message": "Wrong request",
            "id": None,
        }))
    passes = Passes.objects.filter(by_user__email=us_email)
    result = {}
    for i in passes:
        photos = []
        if Photo.objects.filter(mpass=i).exists():
            photos_qs = Photo.objects.filter(mpass=i)
            for j in photos_qs:
                photos.append(j.photo)
        result.update({i.id: {
            "title": i.name,
            "latitude": i.latitude,
            "latitude_zone": i.latitude_zone,
            "longitude": i.longitude,
            "longitude_zone": i.longitude_zone,
            "height": i.height,
            "winter_dif": i.winter_dif,
            "spring_dif": i.spring_dif,
            "summer_dif": i.summer_dif,
            "autumn_dif": i.autumn_dif,
            "activities": i.activ,
            "zone": i.zone.name,
            "g_zone": i.zone.global_zone.name,
            "status": i.status,
            "photos": photos,
        }})
    return HttpResponse(json.dumps(result))
