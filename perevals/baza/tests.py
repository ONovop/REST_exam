from django.test import TestCase, RequestFactory
from .views import submitData, get_patch
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
        request = json.loads(self.factory.post('submitdata/', body, content_type='application/json').body)
        print('request is ', request)
        url = 'submitdata/3/'
        response = json.loads(self.factory.get(url).body)
        print('response is', response)

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
