# encoding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html', dict())


def register(request):
    return render(request, 'frontend/order.html', dict())


def popular_Restaurents(request):
    return render(request, 'frontend/popular-Restaurents.html', dict())


def order(request):
    return render(request, 'frontend/order.html', dict())


def login(request):
    return render(request, 'frontend/login.html', dict())


def contact(request):
    return render(request, 'frontend/contact.html', dict())
