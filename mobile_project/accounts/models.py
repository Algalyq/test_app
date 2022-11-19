
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator
from django.db.models import Q
import random
import os
import requests


class CustomUserManager(BaseUserManager):
	def create_user(self, phone, password=None):
		if not phone:
			raise ValueError('User must have a phone number')
		
		user = self.model(phone=phone)

		user.is_staff=False
		user.is_admin=False
		user.is_active=True
		user.save(using=self._db)
		return user


	def create_superuser(self, phone, password=None):
		user = self.create_user(phone, password=password)
		user.is_staff=True
		user.is_admin=True
		user.save(using=self._db)
		return user



class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator( regex   =r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone       = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    name        = models.CharField(max_length = 20, blank = True, null = True)

    standard    = models.CharField(max_length = 3, blank = True, null = True)
    score       = models.IntegerField(default = 16)

    first_login = models.BooleanField(default=False)

    is_active      = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=False)
    is_admin       = models.BooleanField(default=False)

    timestamp   = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'phone'

    
    objects = CustomUserManager()
    def __str__(self):
    	return self.phone

    def has_perm(self, perm, obj=None):
    	return True

    def has_module_perms(self, app_label):
    	return True

    class Meta:
        verbose_name_plural = "User"
    @property
    def is_superuser(self):
        return self.is_admin



class PhoneOTP(models.Model):
    phone_regex = RegexValidator( regex   =r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone       = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    otp         = models.CharField(max_length = 9, blank = True, null= True)

    count       = models.IntegerField(default = 0, help_text = 'Number of otp sent')
    logged      = models.BooleanField(default = False, help_text = 'If otp verification got successful')
    forgot      = models.BooleanField(default = False, help_text = 'only true for forgot password')
    forgot_logged = models.BooleanField(default = False, help_text = 'Only true if validdate otp forgot get successful')
   

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)


    class Meta:
        verbose_name_plural = "Phone"