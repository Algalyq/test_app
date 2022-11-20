
from django.contrib import admin
from rent_app.models import Boot_directory,Ski_directory,Subsc_directory, Resort_directory,Resort_contact,WeatherModel
from django.contrib.gis.admin import OSMGeoAdmin

#Other admin page URL = 'http://127.0.0.1:8000/rent_admin/ >

class RentAdminArea(admin.AdminSite):
    site_header = "Rent Admin Area"
rent_admin = RentAdminArea(name='RentAdmin')

class SubscAdmin(admin.ModelAdmin):
    list_display = ('resort_subsc','subscription','cost_subscr')
rent_admin.register(Subsc_directory,SubscAdmin)

#<


admin.site.register(Subsc_directory,SubscAdmin)
class SkiAdmin(admin.ModelAdmin):
    list_display = ('resort_ski', 'ski_size')
rent_admin.register(Ski_directory, SkiAdmin)

@admin.register(Boot_directory)
class Boot_admin(admin.ModelAdmin):
    list_display = ('boots_size','boots_count','boots_rent_cost')

@admin.register(Ski_directory)
class SkiAdmin(admin.ModelAdmin):
    list_display = ('ski_size','ski_count','ski_rent_cost')

@admin.register(Resort_directory)
class ResortAdmin(admin.ModelAdmin):
    list_display = ('resort_name','resort_address')
@admin.register(Resort_contact)
class ResortAdmin(OSMGeoAdmin):
    list_display = ('id','contact_phone')


@admin.register(WeatherModel)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('resort_address','description','temp')