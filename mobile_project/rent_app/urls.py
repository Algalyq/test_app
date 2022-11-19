
from django.contrib import admin
from django.urls import path, include
from .views import ResortView
urlpatterns = [

    path('resort/',ResortView.as_view())
    
]

