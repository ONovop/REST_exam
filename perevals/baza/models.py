from django.db import models
from django.contrib.postgres.fields import ArrayField

class DBUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

class GlobalZones(models.Model):
    name = models.CharField(max_length=50)

class LocalZones(models.Model):
    name = models.CharField(max_length=50)
    global_zone = models.ForeignKey(GlobalZones, on_delete=models.CASCADE)

class Passes(models.Model):

    LAT_ZONES = [('N', 'северная'), ('S', 'южная')]
    LONG_ZONES = [('W', 'западная'), ('E', 'восточная')]
    DIFFICULT_LEVELS = [
        ('1A', '1А'),
        ('1B', '1Б'),
        ('2A', '2А'),
        ('2B', '2Б'),
        ('3A', '3А'),
        ('3B', '3Б'),
        ('4A', '4А'),
        ('4B', '4Б'),
        ('5A', '5А'),
        ('5B', '5Б'),
        ('6A', '6А'),
        ('6B', '6Б'),
    ]
    ACTIVITIES = [
        ('FT', 'пешком'),
        ('SK', 'лыжи'),
        ('CN', 'катамаран'),
        ('KK', 'байдарка'),
        ('RT', 'плот'),
        ('RR', 'сплав'),
        ('BC', 'велосипед'),
        ('AU', 'автомобиль'),
        ('MB', 'мотоцикл'),
        ('SA', 'парус'),
        ('HR', 'верхом'),
    ]
    STATUSES = [
        ('N', 'new'),
        ('P', 'pending'),
        ('A', 'accepted'),
        ('R', 'rejected'),
    ]

    name = models.CharField(max_length=50)
    time_add = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    latitude_zone = models.CharField(max_length=1, choices=LAT_ZONES, default='N')
    longitude = models.FloatField()
    longitude_zone = models.CharField(max_length=1, choices=LONG_ZONES, default='E')
    height = models.IntegerField()
    by_user = models.ForeignKey(DBUser, on_delete=models.CASCADE)
    zone = models.ForeignKey(LocalZones, on_delete=models.CASCADE)
    winter_dif = models.CharField(max_length=2, choices=DIFFICULT_LEVELS)
    spring_dif = models.CharField(max_length=2, choices=DIFFICULT_LEVELS)
    summer_dif = models.CharField(max_length=2, choices=DIFFICULT_LEVELS)
    autumn_dif = models.CharField(max_length=2, choices=DIFFICULT_LEVELS)
    activ = ArrayField(models.CharField(max_length=2, choices=ACTIVITIES), size=11)
    status = models.CharField(max_length=1, choices=STATUSES, default='N')

class Photo(models.Model):
    photo = models.ImageField()
    time_add = models.DateTimeField(auto_now_add=True)
    mpass = models.ForeignKey(Passes, on_delete=models.CASCADE)
