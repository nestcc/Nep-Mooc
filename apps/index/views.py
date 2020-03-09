from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from apps.teacher.controller.register import Register as tchRegister


# Create your views here.

def login(request):
    content = {'user_type': 'student'}
    return render(request, 'index/login.html', content)


def tch_login(request):
    content = {'user_type': 'teacher'}
    return render(request, 'index/login.html', content)


def register(request):
    return HttpResponse('register')


def tch_register(request):
    tch_reg = tchRegister(name='test', password='test', mobile='121312')
    tch_reg.register()
    return HttpResponse('tch_register')


def redirect_home(request):
    return HttpResponseRedirect('/index/login/')
