from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app(request):
    return HttpResponse("welcome to django  aap  page")