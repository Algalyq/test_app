# Generated by Django 3.2.12 on 2022-11-20 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0013_alter_weather_resort_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weather',
            new_name='WeatherModel',
        ),
    ]