from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app3(request):
    return HttpResponse("Welcome to App 3 page of django")