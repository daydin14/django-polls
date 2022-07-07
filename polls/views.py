from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello World Polls Index Page?!</h1>')