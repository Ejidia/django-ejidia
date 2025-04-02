from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse('Hello, World! Am Ejidia Uwabeza, Astudent at Refactory Academy offering a Certificate in Software engineering in python.' )
