#Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from TimelineService import TimelineService as T

def index(request):
	return render(request, 'semanticSearch/index.html',{})

def timeline(request):
	query = request.POST.get('searchQuery')
	t = T()
	timeline = json.dumps(t.ProcessQuery(query))
#	timeline = json.dumps([query])
	return HttpResponse(timeline, content_type='application/json')
