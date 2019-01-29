"""Views for the base app"""

from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')


def auth(request):
	response = {"access_token":"admin","status":"ok"}
	return JsonResponse(response)


def token(request):
	response = {"licenses":[{"id":1,"expirary":0,"type":"Admin","activated":True,"purchase_date":1548114184.1072772,"hwid":"8a489e698bb2e7aee3ec0cd14e1fac0cf03b713f6118c0d8544cc291793d3287"}],"status":"ok"}	
	return JsonResponse(response)

def register(request):
	response = {"success":True,"message":"","status":"ok"}
	return JsonResponse(response)