from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hemanth(request):
    return HttpResponse('<marquee><h1>Hi Hemanth how r u</h1></marquee>')