from django.test import TestCase, RequestFactory
from .views import submitData, get_patch, user_filter
import json

class APITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_post(self):
        body = {
            "title": "test_title",
            "latitude": 45,
            "latitude_zone": "N",
            "longitude": 90,
            "longitude_zone": "E",
            "height": 3000,
            "winter_dif": "1A",
            "spring_dif": "2A",
            "summer_dif": "3A",
            "autumn_dif": "4A",
            "username": "test_user",
            "email": "test@mail.com",
            "phone": "+7-777-777-77-77",
            "photos": [],
        }
        request = self.factory.post('submitdata/', body, content_type='application/json')
        rec_id = json.loads(submitData(request).content)['id']
        request_get = self.factory.get('/submitdata/'+str(rec_id)+'/')
        response = json.loads(get_patch(request_get, pk=rec_id).content)

        self.assertEqual(body['title'], response['title'])
        self.assertEqual(body['latitude'], response['latitude'])
        self.assertEqual(body['latitude_zone'], response['latitude_zone'])
        self.assertEqual(body['longitude'], response['longitude'])
        self.assertEqual(body['longitude_zone'], response['longitude_zone'])
        self.assertEqual(body['height'], response['height'])
        self.assertEqual(body['winter_dif'], response['winter_dif'])
        self.assertEqual(body['spring_dif'], response['spring_dif'])
        self.assertEqual(body['summer_dif'], response['summer_dif'])
        self.assertEqual(body['autumn_dif'], response['autumn_dif'])
        self.assertEqual(body['username'], response['username'])
        self.assertEqual(body['email'], response['email'])
        self.assertEqual(body['phone'], response['phone'])
        self.assertEqual(body['photos'], response['photos'])

    def test_patch(self):
        body = {
            "title": "test_title",
            "latitude": 45,
            "latitude_zone": "N",
            "longitude": 90,
            "longitude_zone": "E",
            "height": 3000,
            "winter_dif": "1A",
            "spring_dif": "2A",
            "summer_dif": "3A",
            "autumn_dif": "4A",
            "username": "test_user",
            "email": "test@mail.com",
            "phone": "+7-777-777-77-77",
            "photos": [],
        }
        body2 = {
            "title": "test_title_2",
            "latitude": 60,
            "latitude_zone": "S",
            "longitude": 120,
            "longitude_zone": "W",
            "height": 4000,
            "winter_dif": "1B",
            "spring_dif": "2B",
            "summer_dif": "3B",
            "autumn_dif": "4B",
            "username": "test_user_2",
            "email": "test@mail.com",
            "phone": "+7-888-888-88-88",
            "photos": [],
        }
        request = self.factory.post('submitdata/', body, content_type='application/json')
        rec_id = json.loads(submitData(request).content)['id']
        request_patch = self.factory.patch('/submitdata/'+str(rec_id)+'/', body2, content_type='application/json')
        patch=json.loads(get_patch(request_patch, pk=rec_id).content)
        request_get = self.factory.get('/submitdata/'+str(rec_id)+'/')
        response = json.loads(get_patch(request_get, pk=rec_id).content)

        self.assertEqual(body2['title'], response['title'])
        self.assertEqual(body2['latitude'], response['latitude'])
        self.assertEqual(body2['latitude_zone'], response['latitude_zone'])
        self.assertEqual(body2['longitude'], response['longitude'])
        self.assertEqual(body2['longitude_zone'], response['longitude_zone'])
        self.assertEqual(body2['height'], response['height'])
        self.assertEqual(body2['winter_dif'], response['winter_dif'])
        self.assertEqual(body2['spring_dif'], response['spring_dif'])
        self.assertEqual(body2['summer_dif'], response['summer_dif'])
        self.assertEqual(body2['autumn_dif'], response['autumn_dif'])
        self.assertEqual(body['username'], response['username'])
        self.assertEqual(body['email'], response['email'])
        self.assertEqual(body['phone'], response['phone'])
        self.assertEqual(body2['photos'], response['photos'])

    def test_user_filter(self):
        body = {
            "title": "test_title",
            "latitude": 45,
            "latitude_zone": "N",
            "longitude": 90,
            "longitude_zone": "E",
            "height": 3000,
            "winter_dif": "1A",
            "spring_dif": "2A",
            "summer_dif": "3A",
            "autumn_dif": "4A",
            "username": "test_user",
            "email": "test@mail.com",
            "phone": "+7-777-777-77-77",
            "photos": [],
        }
        request = self.factory.post('submitdata/', body, content_type='application/json')
        rec_id = json.loads(submitData(request).content)['id']
        request_get = self.factory.get('/submitdata/user/'+body['email']+'/')
        response_full = json.loads(user_filter(request_get, email=body['email']).content)
        response = response_full[str(rec_id)]

        self.assertEqual(body['title'], response['title'])
        self.assertEqual(body['latitude'], response['latitude'])
        self.assertEqual(body['latitude_zone'], response['latitude_zone'])
        self.assertEqual(body['longitude'], response['longitude'])
        self.assertEqual(body['longitude_zone'], response['longitude_zone'])
        self.assertEqual(body['height'], response['height'])
        self.assertEqual(body['winter_dif'], response['winter_dif'])
        self.assertEqual(body['spring_dif'], response['spring_dif'])
        self.assertEqual(body['summer_dif'], response['summer_dif'])
        self.assertEqual(body['autumn_dif'], response['autumn_dif'])
        self.assertEqual(body['photos'], response['photos'])
