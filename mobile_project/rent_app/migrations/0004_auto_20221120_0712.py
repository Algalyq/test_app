# Generated by Django 3.2.12 on 2022-11-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0003_auto_20221120_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temp',
            field=models.IntegerField(blank=True),
        ),
    ]
