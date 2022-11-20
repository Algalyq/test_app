from rest_framework import serializers
from .models import Boot_directory, Ski_directory, Subsc_directory, Resort_directory,Resort_contact,WeatherModel


class ContactSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Resort_contact
        fields = ('id','contact_phone')

class BootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boot_directory
        fields = ('id','boots_size','boots_count','boots_rent_cost')


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherModel.objects.latest('resort_address')
        fields = ('description','temp')

class SkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ski_directory
        fields = ('ski_size','ski_count','ski_rent_cost')


class SubscSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Subsc_directory
        fields = ('subscription','cost_subscr','table_prices')


class ResortSerializer(serializers.ModelSerializer):
    ski = SkiSerializer(many=True)
    subsc = SubscSerializer(many=True)
    boot = BootsSerializer(many=True) 
    contact = ContactSerializer(many=True)
    weather = WeatherSerializer(WeatherModel,many=True)
    class Meta:
        model = Resort_directory
        fields = ['resort_name','resort_address', 'weather','contact','ski','subsc','boot']
