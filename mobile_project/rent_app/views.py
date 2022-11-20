from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Ski_directory, Resort_directory
from .serializers import SkiSerializer, BootsSerializer,SubscSerializer,ResortSerializer
import requests
from .utils import getweather
from rest_framework.response import Response
import json
import time
import asyncio
from .models import Boot_directory, Ski_directory, Subsc_directory, Resort_directory,WeatherModel
class SkiView(APIView):
    def get(self,request):
        ski = Ski_directory.objects.all()
        serializer = SkiSerializer(ski, many=True)
        return Response(serializer.data)

class ResortView(APIView):
    def get(self,request):
        test = Resort_directory.objects.all()
        if True:
            resort = Resort_directory.objects.values_list('resort_address')
            len_res = len(resort)
            for value in resort:
                for key in range(0,len_res-1):
                    data = asyncio.run(getweather(str(value[key])))
                    place =Resort_directory.objects.get(resort_address=value[key])
                    weather = WeatherModel.create(place,data['description'],data['temp'])  
                    weather.save()
        serializer = ResortSerializer(test,many=True)
        serializer_list = list(serializer.data)
        

        return Response(serializer_list)