from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2(request):
    return HttpResponse("Welcome to App 2 page of django")