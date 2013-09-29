#Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

def index(request):
	return render(request, 'semanticSearch/index.html',{})

def timeline(request):
	timeline = json.dumps(['foo'])
	return HttpResponse(timeline, content_type='application/json')
	#return render(request, 'semanticSearch/index2.html',{'timeline':timeline})
