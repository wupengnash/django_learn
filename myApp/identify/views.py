from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)

def index(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)
