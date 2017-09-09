#encoding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def hellow(request):
    return render(request, 'frontend/index.html', dict())
