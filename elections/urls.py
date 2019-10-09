from django.urls import path,include
from . import views

app_name = 'elections'
urlpatterns = [
    path('',views.index,name = 'home'),
    path('poll/<str:area>',views.areas),
    path('poll/choice/<str:poll_id>',views.choice), #<str:area>이 부분이 없어지는데 get방식이라 그런가??
    path('poll/choice/result/<str:area>',views.result), #url를 추가하는 방식으로 하면 <str>부분은 날라간다..
]
