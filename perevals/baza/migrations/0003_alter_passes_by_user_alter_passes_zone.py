# Generated by Django 4.1.6 on 2023-02-03 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0002_alter_passes_height_alter_passes_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passes',
            name='by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dbusers', to='baza.dbuser'),
        ),
        migrations.AlterField(
            model_name='passes',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zones', to='baza.localzones'),
        ),
    ]
