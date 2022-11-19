from rest_framework import serializers
from .models import Boot_directory, Ski_directory,Prices, Subsc_directory, Resort_directory,Resort_contact
from .utils import weather_api

class ContactSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Resort_contact
        fields = ('id','contact_phone')

class BootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boot_directory
        fields = ('id','boots_size','boots_count','boots_rent_cost')


class WeatherSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=20)
    temp = serializers.IntegerField()
    wind = serializers.IntegerField()
    cloud = serializers.IntegerField()
    lon = serializers.IntegerField()
    lat = serializers.IntegerField()
    

class SkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ski_directory
        fields = ('ski_size','ski_count','ski_rent_cost')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ('__all__')     

class SubscSerializer(serializers.ModelSerializer):

    prices = PriceSerializer(many=True)
    class Meta: 
        model = Subsc_directory
        fields = ('subscription','cost_subscr','table_prices','prices')


class ResortSerializer(serializers.ModelSerializer):
    ski = SkiSerializer(many=True)
    subsc = SubscSerializer(many=True)
    boot = BootsSerializer(many=True) 
    contact = ContactSerializer(many=True)
    class Meta:
        model = Resort_directory
        fields = ['resort_name','resort_address', 'contact','ski','subsc','boot']
