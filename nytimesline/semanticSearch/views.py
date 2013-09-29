#Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

def index(request):
	return render(request, 'semanticSearch/index.html',{})

def timeline(request):
	query = request.POST.get('searchQuery')
	timeline = json.dumps([query])
	return HttpResponse(timeline, content_type='application/json')
