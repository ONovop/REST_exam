# Generated by Django 4.1.6 on 2023-02-02 07:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalZones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LocalZones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('global_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.globalzones')),
            ],
        ),
        migrations.CreateModel(
            name='Passes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.FloatField()),
                ('latitude_zone', models.CharField(choices=[('N', 'северная'), ('S', 'южная')], default='N', max_length=1)),
                ('longitude', models.FloatField()),
                ('longitude_zone', models.CharField(choices=[('W', 'западная'), ('E', 'восточная')], default='E', max_length=1)),
                ('height', models.IntegerField()),
                ('winter_dif', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2)),
                ('spring_dif', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2)),
                ('summer_dif', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2)),
                ('autumn_dif', models.CharField(choices=[('1A', '1А'), ('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2)),
                ('activ', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('FT', 'пешком'), ('SK', 'лыжи'), ('CN', 'катамаран'), ('KK', 'байдарка'), ('RT', 'плот'), ('RR', 'сплав'), ('BC', 'велосипед'), ('AU', 'автомобиль'), ('MB', 'мотоцикл'), ('SA', 'парус'), ('HR', 'верхом')], max_length=2), size=11)),
                ('status', models.CharField(choices=[('N', 'new'), ('P', 'pending'), ('A', 'accepted'), ('R', 'rejected')], default='N', max_length=1)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.dbuser')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.localzones')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('mpass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.passes')),
            ],
        ),
    ]
