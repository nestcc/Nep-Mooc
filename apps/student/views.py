from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return HttpResponse('login_form')


def index(request):
    content = {'class_my_course': '',
               'class_new_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': ''}
    return render(request, 'student/index.html', content)


def my_course(request):
    return HttpResponse()


def search_course(request):
    return HttpResponse()


def search_user(request):
    return HttpResponse()


def profile(request):
    return HttpResponse()


def play_videos(requests):
    content = {'class_my_course': '',
               'class_new_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'media_path': 'media/10/1-5.mp4'}
    return render(requests, 'student/play_video.html', content)