#codeing:UTF8
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def hello(request):
    return HttpResponse("wocao")
# Create your views here.

def hello2(request,num):
    try:
        t = int(num)
    except TypeError  as e:
        raise Http404
    else:
        pass

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(request,a,b):
    return HttpResponse(str(int(a) + int(b)))
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
