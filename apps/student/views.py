from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .controller.course import Course
from .controller.oneStatus import new_status, LearnStatus


# Create your views here.

def login(request):
    return HttpResponse('login_form')


def index(request):
    content = {'class_my_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': ''}
    return render(request, 'student/index.html', content)


def my_course(request):
    content = {'class_my_course': 'layui-this',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': ''}
    return HttpResponse()


def search_course(request, page=0):
    search_obj = Course()
    content = {'class_my_course': '',
               'class_search_course': 'layui-this',
               'class_search_user': '',
               'class_profile': '',
               'item_number': search_obj.get_item_number(),
               'cour_list': search_obj.all_course(number=6, page=page)}
    return render(request, 'student/new_course.html', content)


def search_user(request):
    content = {'class_my_course': '',
               'class_search_course': '',
               'class_search_user': 'layui-this',
               'class_profile': ''}
    return HttpResponse()


def profile(request):
    content = {'class_my_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': 'layui-this'}
    return HttpResponse()


def play_videos(requests):
    content = {'class_my_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'media_path': 'media/10/1-5.mp4'}
    return HttpResponse()


def show_cour_info(request, id):
    cour_obj = Course(id=id)
    print(cour_obj.get_cour_info())
    return JsonResponse(cour_obj.get_cour_info())


def join_course(request):
    result = new_status(id_stu=1, id_cour=request.POST['id_cour'])
    print(result)
    return JsonResponse(result)