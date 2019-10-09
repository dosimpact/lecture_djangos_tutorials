from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Candidate,Choice,Poll
from django.db.models import Sum
import datetime
"""

def index(request):
    str = ""
    candidates = Candidate.objects.all()
    for candidate in candidates:
        str += " <b>이름 : {} </b>지역 {}: 번호 : {}<br> 소개 {} <br><hr>".format(candidate.name,candidate.area,candidate.party_number,candidate.introduction)
    return HttpResponse(str)
    """

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request,'elections/index.html',context)



def areas(request,area):
    today = datetime.datetime.now()
    #해당 지역구 여론조사를 보여준다. 1. 지역 2. 현재시간 맞는지.
    try:
        candidates = Candidate.objects.filter(area = area)
        poll = Poll.objects.get(area = area, start_date__lte = today,end_date__gte = today)  
    except:
        candidates = None
        poll = None
    return render(request,'elections/area.html',context = {'candidates':candidates,'poll':poll,'area':area})
#path('poll/choice/<str:poll_id>',views.choice



def choice(request,poll_id):
    candidate_id = request.POST['choice']
    poll = Poll.objects.get(pk = poll_id)
    try:
        choice = Choice.objects.get(candidate_id = candidate_id,poll_id = poll_id)
        choice.votes += 1
        choice.save() #항상 세이브 하는거 잊지 말귀
    except:
        new_choice = Choice(candidate_id = candidate_id,poll_id = poll_id, votes = 0)
        new_choice.votes += 1
        new_choice.save() 
    return HttpResponseRedirect('result/{}'.format(poll.area))

def result(request,area): #
    context = {}
    candidates = Candidate.objects.filter(area = area) #
    poll_rows = [] #
    polls = Poll.objects.filter(area = area)
    
    for poll in polls:
        poll_row = {}
        poll_row['start_date'] = poll.start_date
        poll_row['end_date'] = poll.end_date
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        poll_row['total_votes'] = total_votes['votes__sum']

        rates = []
        for candidate in candidates:
            choice = Choice.objects.get(candidate_id = candidate.id,poll_id = poll.id)
            rates.append(   round( choice.votes * 100 / poll_row['total_votes'] ,3))
        poll_row['rates'] = rates
        poll_rows.append(poll_row)
    # 지역 데이터를 받아서 -> 그 지역에 해당하는 후보들 /
    # 기간 | 후보들
    # 시작일~종료일 | 후보들 득표율
    return render(request,'elections/result.html',context = {'area':area,'candidates':candidates,'poll_rows':poll_rows})