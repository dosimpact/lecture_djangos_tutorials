from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'video'
urlpatterns = [
    path('',views.video_list,name = 'list'),
    path('new/',views.video_new,name = 'new'),
    path('<str:video_id>',views.video_detail,name = 'detail'),
]
