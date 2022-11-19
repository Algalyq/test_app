
from django.contrib import admin
from rent_app.models import Boot_directory,Ski_directory,Subsc_directory, Resort_directory,Resort_contact, Prices
from django.contrib.gis.admin import OSMGeoAdmin

class RentAdminArea(admin.AdminSite):
    site_header = "Rent Admin Area"

rent_admin = RentAdminArea(name='RentAdmin')

class SubscAdmin(admin.ModelAdmin):
    list_display = ('resort_subsc','subscription','cost_subscr')
rent_admin.register(Subsc_directory,SubscAdmin)

class SkiAdmin(admin.ModelAdmin):
    list_display = ('resort_ski', 'ski_size')
rent_admin.register(Ski_directory, SkiAdmin)
class Boot_admin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = 'Boots'
        list_display = ('boots_size','boots_count','boots_rent_cost')


admin.site.register(Boot_directory)
admin.site.register(Ski_directory)
admin.site.register(Subsc_directory)
admin.site.register(Resort_directory)
admin.site.register(Prices)
@admin.register(Resort_contact)
class ResortAdmin(OSMGeoAdmin):
    list_display = ('id','contact_phone')