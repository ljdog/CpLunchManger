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
        user_name = forms.CharField()
        user_email = forms.CharField()
        user_passwd = forms.CharField()
        passwd_check = forms.CharField()
        user_nice = forms.CharField()

    if not request.POST:
        return register(request)

    form = TestForm(request.POST)

    if not form.is_valid():
        print form
        return HttpResponse('is vail error')

    user_name = form.cleaned_data['user_name']
    user_passwd = form.cleaned_data['user_passwd']
    passwd_check = form.cleaned_data['passwd_check']
    user_email = form.cleaned_data['user_email']
    user_nice = form.cleaned_data['user_nice']
    from mg.forms import AddUserForm, User, RoleList

    if User.objects.filter(username=user_name):
        return HttpResponse(u'用户已经存在')

    if user_passwd != passwd_check:
        return HttpResponse(u'2次输入密码不一致')

    obj = User()
    obj.email = user_email
    obj.username = user_name
    obj.nickname = user_nice
    obj.is_active = True
    obj.set_password(user_passwd)
    find_rst = RoleList.objects.filter(name=u"普通用户")
    if not find_rst:
        r = RoleList()
        r.name = u"普通用户"
        r.save()
        find_rst = RoleList.objects.filter(name=u"普通用户")
    if find_rst[0]:
        obj.role = find_rst[0]

    obj.save()

    return HttpResponse('0k')

def user_info(request):
    return render(request, 'frontend/user_view.html', dict())
