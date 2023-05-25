from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def strings (request):
    return HttpResponse('string one output')
