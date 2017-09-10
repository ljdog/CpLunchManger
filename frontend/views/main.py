# encoding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html', dict())


def index2(request):
    return index(request)
    # return render(request, 'frontend/index.html', dict())

def register(request):
    return render(request, 'frontend/register.html', dict())


def popular_restaurents(request):
    return render(request, 'frontend/popular-Restaurents.html', dict())


def order(request):
    return render(request, 'frontend/order.html', dict())


def login(request):
    return render(request, 'frontend/login.html', dict())


def contact(request):
    return render(request, 'frontend/contact.html', dict())

def user_register(request):
    from django import forms
    class TestForm(forms.Form):
        """
        查询桌子信息
        """
        user_name = forms.CharField()
        user_email = forms.CharField()
        user_passwd = forms.CharField()

    if not request.POST:
        return register(request)

    form = TestForm(request.POST)

    if not form.is_valid():
        print form
        return HttpResponse('is vail error')

    user_name = form.cleaned_data['user_name']
    user_passwd = form.cleaned_data['user_passwd']
    user_email = form.cleaned_data['user_email']
    from mg.models import User
    from mg.forms import AddUserForm, User
    # obj = AddUserForm()
    # obj.username = user_name
    # obj.email = user_email
    # obj.password = user_passwd
    obj = User()
    obj.email = user_email
    obj.username = user_name
    obj.is_active = True
    obj.set_password(user_passwd)
    # obj.set_password(user_passwd)
    obj.save()
    # obj.create_user(user_email,user_name, user_passwd)
    # obj.save()

    return HttpResponse('0k')
