#Create your views here.
from django.shortcuts import render, get_object_or_404
from semanticSearch.models import SemanticService

def index(request):
	return render(request, 'semanticSearch/index.html',{})

