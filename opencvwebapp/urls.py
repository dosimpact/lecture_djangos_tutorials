from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'opencvwebapp'
urlpatterns = [
    path('',views.index,name = 'main'),
    path('uimage/',views.uimage,name = 'uimage'),
    path('dface/',views.dface,name = 'dface'),
]