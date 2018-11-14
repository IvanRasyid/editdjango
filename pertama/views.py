from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myView(Request):
    return HttpResponse ('Alhamdulillah Djangonya bekerja')
