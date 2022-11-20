
from django.contrib import admin
from django.urls import path, include
from rent_app.admin import rent_admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('accounts.urls')),
    path('rent/', include('rent_app.urls')),
    path("rent_admin/",rent_admin.urls)
]
