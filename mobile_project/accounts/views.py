from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
import requests
from rest_framework import exceptions
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import APIException
from .utils import send_otp,post_otp, check_otp
from .authentication import create_access_token,decode_access_token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import User, PhoneOTP
from rest_framework.authentication import get_authorization_header
from .serializers import (CreateUserSerialzier, 
                        UserSerializer, SerOTP)

class Test(APIView):
    
 
    def post(self,request):
        phone = self.request.data.get('phone')
        otp = self.request.data.get('otp')
        
        if phone and otp: 
            serializer = check_otp(self, request)
            
            return Response(serializer.data)
        elif phone:
            serializer = post_otp(self, request)
            return Response(serializer.data)

        
    
        # if phone: 
        #     phone_number = str(phone)
        #     user = User.objects.filter(phone=phone_number)
            
        #     if user.exists():
        #         return Response({'status':False})
        #     else: 
        #      # Here asap will be twilio (sms message)
        #         otp
        # return Response({"status": phone})





# class Register(APIView):
#     # permission_classes_by_action = {'create': [permissions.AllowAny]}
#     def post(self, *args, **kwargs):
#         phone = self.request.data.get('phone', False)
#         password = self.request.data.get('password', False)
        
#         if phone and password:
#             phone = str(phone)
#             user = User.objects.filter(phone__iexact = phone)

#             if user.exists():
#                 return Response({
#                     'status': False, 
#                     'detail': 'Phone Number already have account associated. Kindly try forgot password'
#                     })

#             else:
#                 old = PhoneOTP.objects.filter(phone__iexact=phone)
#                 if old.exists():
#                     old=old.first()

#                     if old.logged:
#                         temp_data = {'phone':phone,'password':password}
#                         serializer = CreateUserSerialzier(data=temp_data)
                        
#                         serializer.is_valid(raise_exception = True)
#                         user = serializer.save()

#                         token = Token.objects.create(user=user)
#                         old.delete()
#                         return Response({"token": token.key})

#                     else:
#                         return Response({
#                             'status': False,
#                             'detail': 'Your otp was not verified earlier. Please go back and verify otp'

#                         })

#                 else:
#                     return Response({
#                     'status' : False,
#                     'detail' : 'Phone number not recognised. Kindly request a new otp with this number'
#                 })

#         else:
#             return Response({
#                 'status' : 'False',
#                 'detail' : 'Either phone or password was not recieved in Post request'
#             })


class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(phone=request.data['phone']).first()

        if not user:
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)

        response = Response()

        response.data = {
            'token': access_token
        }

        return response

