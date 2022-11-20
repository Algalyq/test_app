
from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
from accounts.models import User
from .utils import getweather
from datetime import datetime
import asyncio
SUBSCRIPTION_DIR = [
    ('Econom','Econom'),
    ('Business','Business'),
]


class Resort_directory(models.Model):
    resort_name = models.CharField(max_length=255, blank=False)
    resort_address = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.resort_name

    class Meta:
        verbose_name_plural = 'Resorts'

class Subsc_directory(models.Model):
    resort_subsc = models.ForeignKey(Resort_directory,related_name='subsc',on_delete=models.CASCADE)
    subscription = models.CharField(choices=SUBSCRIPTION_DIR,max_length=20)
    cost_subscr = models.PositiveIntegerField()


    class Meta:
        verbose_name_plural = 'Subscription'

class Ski_directory(models.Model):
    resort_ski = models.ForeignKey(Resort_directory,related_name='ski',on_delete=models.CASCADE)
    ski_size = models.PositiveIntegerField()
    ski_count = models.PositiveIntegerField()
    ski_rent_cost = models.PositiveIntegerField()


    class Meta:
        verbose_name_plural = 'Ski'
    
class Boot_directory(models.Model):
    resort_boot = models.ForeignKey(Resort_directory,related_name='boot',on_delete=models.CASCADE)
    boots_size = models.PositiveIntegerField()
    boots_count = models.PositiveIntegerField()
    boots_rent_cost = models.PositiveIntegerField()


    class Meta:
        verbose_name_plural = 'Boots'
       
class Resort_contact(models.Model):
    resort_contact = models.ForeignKey(Resort_directory,related_name='contact', on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)

    class Meta:
        verbose_name_plural = 'Contacts'

class Payment_history(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_cost = models.PositiveIntegerField()


    class Meta:
        verbose_name_plural = 'Payment history'

class WeatherModel(models.Model):
    resort_address = models.ForeignKey(Resort_directory,related_name='weather', on_delete=models.CASCADE)
    description = models.CharField(max_length=120, blank=True)
    temp = models.IntegerField(blank=True,default=0)


    @classmethod
    def create(cls,resort_address,description,temp):
        weather = cls(resort_address=resort_address,description=description,temp=temp)
        return weather
