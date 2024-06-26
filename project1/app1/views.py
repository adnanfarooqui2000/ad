from django.shortcuts import render
from django.http import HttpResponse
def app1(request):
    return HttpResponse("Welcome to App 1 page of django")