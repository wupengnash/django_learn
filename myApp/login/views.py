from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def register(request):
    name_dict = {'wup': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)
