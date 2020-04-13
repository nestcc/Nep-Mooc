from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from index.models import NepCourse, NepLearnStatus, NepSection
from .controller.course import Course
from .controller.allStatus import *


# Create your views here.

def login(request):
    return HttpResponse('login_form')


def index(request):
    content = {'class_my_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': ''}
    return render(request, 'student/index.html', content)


def my_course(request, page=1):
    cour_obj = Course()
    stu_id = request.COOKIES['stu_id']
    content = {'class_my_course': 'layui-this',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'item_number': cour_obj.get_item_number(stu_id=stu_id),
               'cour_list': cour_obj.stu_cour(number=4, page=page, stu_id=stu_id)}

    return render(request, 'student/my_course.html', content)


def search_course(request, page=1):
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
    return render(request, 'student/index.html', content)


def profile(request):
    content = {'class_my_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': 'layui-this'}
    return render(request, 'student/index.html', content)


def show_cour_info(request, id):
    cour_obj = Course(id=id)
    return JsonResponse(cour_obj.get_cour_info())

def show_cour_detail(request, id):
    cour_obj = NepCourse.objects.get(pk=id)
    content = {'cour': cour_obj,
               'stu_num': NepLearnStatus.objects.filter(course_id=id).count(),
               'sect_num': NepSection.objects.filter(sect_cour_id=id).count()}
    return render(request, 'student/course_detail.html', content)

def join_course(request):
    stu_id = request.COOKIES['stu_id']

    result = new_status(id_stu=stu_id, id_cour=request.POST['id_cour'])
    print(result)
    return JsonResponse(result)

def course_page(request, id):
    content = {'class_my_course': 'layui-this',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': ''}
    if not NepCourse.objects.get(pk=id).cour_avilable:
        return render(request, 'student/course_not_avai.html', content)
    else:
        content['section_list'] = NepSection.objects.filter(sect_cour_id=id).order_by('sect_tag')
        return render(request, 'student/course_page.html', content)

def get_learned_sect(request):
    stu_id = request.COOKIES['stu_id']
    return JsonResponse(get_learned(cour_id=request.POST['cour_id'], stu_id=stu_id))

def learn_view(request, sect_id):
    stu_id = request.COOKIES['stu_id']
    sect_obj = NepSection.objects.get(pk=sect_id)
    content = {'class_my_course': 'layui-this',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'sect_tag': sect_obj.sect_tag,
               'sect_name': sect_obj.sect_name,
               'sect_text': sect_obj.sect_text,
               'sect_media': sect_obj.sect_media}

    before_learn(sect_id=sect_id, stu_id=stu_id)

    return render(request, 'student/learning.html', content)

def finish_sect(request):
    stu_id = request.COOKIES['stu_id']
    json_return = finish_sect_handler(sect_id=request.POST['sect_id'], stu_id=stu_id)
    return JsonResponse(json_return)

def search_course_by_info(request, info='', page=1):
    search_obj = Course()
    content = {'class_my_course': '',
               'class_search_course': 'layui-this',
               'class_search_user': '',
               'class_profile': '',
               'item_number': search_obj.get_item_number(info=info),
               'cour_list': search_obj.all_course(number=6, page=page, info=info)}
    return render(request, 'student/new_course.html', content)