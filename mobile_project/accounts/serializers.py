from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model

User = get_user_model()



class CreateUserSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','phone')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone' )


    def validate(self, attrs):
        phone = attrs.get('phone')
        if phone:
            if User.objects.filter(phone=phone).exists():
                if User.objects.filter(phone=phone).count() > 1:
                    msg = {'detail': 'Phone number is already associated with another user. Try a new one.', 'status':False}
                    raise serializers.ValidationError(msg)

        return attrs


    def update(self, instance, validated_data):
        instance.phone = validated_data['phone']
        instance.name = validated_data['name']
        instance.standard = validated_data['standard']
        instance.score = validated_data['score']

        instance.save()
        return instance

class SerOTP(serializers.Serializer):
    phone = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)