from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("wocao")
# Create your views here.
