from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def postgresql(request):
    return HttpResponse('postgresql mini project')