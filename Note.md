# 암기노트

```python

#암기 노트
 
```

```python 
#장고 초기 셋팅
pip install Django
django-admin startproject mysite
python manage.py startapp elections
setting에 앱 추가했다고 명시하기
```
 
```python 
#urls
from django.urls import path,include
path('',include('elections.urls')),
from . import views
path('',views.index),
path('area/<str:area>/',views.areas)
```

```python
#views
from django.http import HttpResponse
return HttpResponse('HI')
 
from django.http import HttpResponseRedirect
 
from django.shortcuts import render
return render(request,'elections/index.html',context)
 
def index(request):
def area(request,area): # path의 area변수명과 url의 area변수가 맞는게 있어야함!!
 
selections = request.POST['choice']
``` 

```python
#DB
from django.db import models
class Candidate(models.Model):
    name = models.CharField(max_length = 10)
    #TextField,IntegerField(default = 0),DateTimeField(),ForeignKey(Poll,on_delete = models.CASCADE)
 
    def __str__(self):
        return self.name
 
python manage.py createmigrations
python manage.py migrate
python manage.py createsuperuser
admin등록
admin.site.register(Candidate)
 
Candidate.objects.all()                                                                  # 리스트로 모두 반환
Candidate.objects.filter(name='KDY)                                                      #리스트로 반환 
-> <QuerySet [<Candidate: 오바마>, <Candidate: 힐러리>, <Candidate: 트럼프>]>   <class 'django.db.models.query.QuerySet'>
Candidate.objects.get(area = area, start_date__lte = today,end_date__gte = today)        #하나의 원소로 반환(가장 들어 맞는 하나!)
-> Poll object (1)   <class 'elections.models.Poll'>
Poll.objects.get(pk = poll)
Choice.objects.get(candidate_id = <str>) # get으로 외래키를 넣는데, 인스턴스가 아닌, 인스턴스.id 를 넣음…
 
from django.db.models import Sum
total_vote = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
result['total_votes'] = total_vote['votes__sum']
 
new_Can = Candidate(name = 'KDY')
new_Can.save()
 
from django.db.models import Sum
```

```python
#HTML 태그
 
<form action = "/poll/{poll.id}/" method = "post">
    {% csrf_token %}
        <button name = "choice" value = "{{candidate.id}}">선택</button>
</from> 
 
 
<a class="btn btn-primary btn-lg" href="poll/1" role="button">되돌아가기</a>
이거는 url이 누적이 되고
<a class="btn btn-primary btn-lg" href="/poll/1" role="button">되돌아가기</a>
이거는 url이 (도메인은 유지한채로) 리스스 경로를 처음부터 시작한다.
<a class="btn btn-primary btn-lg" href="http://~~" role="button">되돌아가기</a>
이거는 url 도메인부터 다른곳으로 이동한다.
```
```python
#HTML django 스크립트
 
반복
{% for candidate in candidates %}
...{{candidate.name}}...
{% endfor %}
 
분기
{% if poll %}
{% else %}
{% endif %}
 
상속
{% block title %} {% endblock %}
{% block body %} {% endblock %}
 
{% extends "elections/layout.html" %}
{% block title %}{% endblock %}
{% block body %} {% ennblock %}
```

```python
#그외
import datetime
today = datetime.datetime.now()
```

```python
 
#깃 사용법
cd ./~
git init
git config --global user.name “DosImpact”
git config --global user.email “ypd03008@gmail.com”
nano .gitignore
 
git commit -m “my first~~”
git remote add origin <git URL>
git push -u origin master
 
git status
git add -all .
git commit -m “changed HTML File”
git push
"""
```
```
DosImpact~

```
