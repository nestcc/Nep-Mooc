from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from index.controller.usrLogin import *

# Create your views here.

def stu_login_view(request):
    if request.COOKIES.__contains__('stu_id'):
        return HttpResponseRedirect('/student/index/')
    elif request.COOKIES.__contains__('tch_id'):
        return HttpResponseRedirect('/teacher/index/')
    else:
        content = {'user_type': 'student',
                   'change_type_href': '/index/tch_login/'}
        return render(request, 'index/login.html', content)


def tch_login_view(request):
    if request.COOKIES.__contains__('stu_id'):
        return HttpResponseRedirect('/student/index/')
    elif request.COOKIES.__contains__('tch_id'):
        return HttpResponseRedirect('/teacher/index/')
    else:
        content = {'user_type': 'teacher',
                   'change_type_href': '/index/stu_login/'}
        return render(request, 'index/login.html', content)

def stu_login(request):
    stu_json = stu_login_by_mobile(stu_mobile=request.POST['mobile'], stu_pwd=request.POST['password'])
    resp = JsonResponse(stu_json)
    if stu_json['status'] == 'SUCCESS':
        resp.set_cookie(key='stu_id', value=stu_json['stu_id'])
        resp.delete_cookie(key='tch_id')
    return resp

def tch_login(request):
    tch_json = tch_login_by_mobile(tch_mobile=request.POST['mobile'], tch_pwd=request.POST['password'])
    reps = JsonResponse(tch_json)
    if tch_json['status'] == 'SUCCESS':
        reps.set_cookie(key='tch_id', value=tch_json['tch_id'])
        reps.delete_cookie(key='stu_id')
    return reps

def stu_register_view(request):
    return HttpResponse('register')


def tch_register_view(request):
    return HttpResponse('tch_register')

def log_out(request):
    reps = HttpResponseRedirect('/')
    reps.delete_cookie(key='stu_id')
    reps.delete_cookie(key='tch_id')
    print(reps.cookies)
    return reps

def redirect_home(request):
    return HttpResponseRedirect('/index/stu_login/')
