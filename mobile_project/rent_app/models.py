
from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
SUBSCRIPTION_DIR = [
    ('Econom','Econom'),
    ('Business','Business'),
]

MY_CHOICES2 = (('Комплект: Лыжи с ботинками и палками или сноуборд с ботинками', 5000),
               ('Лыжи или сноуборд',3000),
                )

class Resort_directory(models.Model):

    resort_name = models.CharField(max_length=255, blank=False)
    resort_address = models.CharField(max_length=1024)
    def __str__(self):
        return self.resort_name
    
class Subsc_directory(models.Model):
    resort_subsc = models.ForeignKey(Resort_directory,related_name='subsc',on_delete=models.CASCADE)
    subscription = models.CharField(choices=SUBSCRIPTION_DIR,max_length=20)
    cost_subscr = models.PositiveIntegerField()
    table_prices = ArrayField(ArrayField(models.CharField(max_length=100),default=list))

class Prices(models.Model):
    subsc_price = models.ForeignKey(Subsc_directory,related_name='prices', on_delete=models.CASCADE)
    name_subsc = ArrayField(models.CharField(max_length=300), default=list)
    price = ArrayField(models.PositiveIntegerField(), default=list)

class Ski_directory(models.Model):
    resort_ski = models.ForeignKey(Resort_directory,related_name='ski',on_delete=models.CASCADE)
    ski_size = models.PositiveIntegerField()
    ski_count = models.PositiveIntegerField()
    ski_rent_cost = models.PositiveIntegerField()
    
class Boot_directory(models.Model):
    resort_boot = models.ForeignKey(Resort_directory,related_name='boot',on_delete=models.CASCADE)
    boots_size = models.PositiveIntegerField()
    boots_count = models.PositiveIntegerField()
    boots_rent_cost = models.PositiveIntegerField()

class Resort_contact(models.Model):
    resort_contact = models.ForeignKey(Resort_directory,related_name='contact', on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    