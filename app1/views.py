from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string (request):
    return HttpResponse('string one output')

def str (request):
    return render(request,'home.html')

