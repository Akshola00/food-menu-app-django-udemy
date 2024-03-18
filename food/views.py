from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hello world')

def item(request):
    return HttpResponse('<h1>this is an item view</h1>')