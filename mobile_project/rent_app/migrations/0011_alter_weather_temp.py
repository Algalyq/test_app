# Generated by Django 3.2.12 on 2022-11-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0010_alter_weather_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='temp',
            field=models.IntegerField(default=0),
        ),
    ]