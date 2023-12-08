
# Create your views here.
from django.http import HttpResponse, request
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world')
