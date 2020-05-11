from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .controller.course import Course
from .controller.section import Section
from .controller import upload
from .controller.otherJson import *
from index.models import *
from teacher.models import NepTeacher


def index(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'num_cour': NepCourse.objects.filter(cour_create_tch_id=request.COOKIES['tch_id']).count()}
    return render(request, 'teacher/index.html', content)


def create_course(request):
    content = {'class_manage_course': '',
               'class_create_course': 'layui-this',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '', }
    return render(request, 'teacher/create_course.html', content)


def user_profile(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': 'layui-this'}
    return render(request, 'teacher/empty.html', content)


def course_list(request):
    #   change teacher id
    cour_list = NepCourse.objects.filter(cour_create_tch=request.COOKIES['tch_id'])
    content = {'class_manage_course': 'layui-this',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'cour_list': cour_list}
    return render(request, 'teacher/manage_course.html', content)


def search_course(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': 'layui-this',
               'class_search_user': '',
               'class_profile': ''}
    return render(request, 'teacher/empty.html', content)


def search_user(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': 'layui-this',
               'class_profile': ''}
    return render(request, 'teacher/empty.html', content)


def new_course(request):
    print(request.POST)
    NewCourse = Course(request.POST, tch_id=request.COOKIES['tch_id'])
    json_return = NewCourse.submit()
    # print(json_return)

    return JsonResponse(json_return)


def course_info(request, id):
    sect_obj = Section()
    # cour_obj = Course({'cour_id': id}, tch_id=request.COOKIES['tch_id'])

    cour_obj = NepCourse.objects.get(id=id, cour_create_tch_id=request.COOKIES['tch_id'])
    cour_date = str(cour_obj.cour_start) + ' - ' + str(cour_obj.cour_end)
    option_num = 'option_' + str(cour_obj.cour_type)

    content = {'class_manage_course': 'layui-this',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',

               'sect_number': sect_obj.find_by_course(cour_id=id)['count'],
               'stu_number': NepLearnStatus.objects.filter(course_id=id).count(),
               'cour_status': '已激活' if cour_obj.cour_avilable else '未激活',
               'cour_status_color': '#009688' if cour_obj.cour_avilable else '#ffb53e',
               'cour_obj': cour_obj,
               'cour_date': cour_date,
               'cour_avai_select': 'checked' if cour_obj.cour_avilable else '',
               'sele' + cour_obj.cour_type: 'selected'
               }
    return render(request, 'teacher/course_info.html', content)


def get_stu_by_cour(request, id):
    return JsonResponse(get_learn_list(course_id=id, limit=int(request.GET['limit']), page=int(request.GET['page'])))


def get_sect_by_cour(request, id):
    return JsonResponse(get_section_list(course_id=id, limit=int(request.GET['limit']), page=int(request.GET['page'])))


def edit_course_info(request, id):
    this_course = NepCourse.objects.get(id=id, cour_create_tch_id=request.COOKIES['tch_id'])
    cour_date = str(this_course.cour_start) + ' - ' + str(this_course.cour_end)
    option_num = 'option_' + str(this_course.cour_type)
    content = {'class_manage_course': 'layui-this',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'cour_id': this_course.id,
               'cour_name': this_course.cour_name,
               'cour_date': cour_date,
               'cour_description': this_course.cour_description,
               'cour_available': this_course.cour_avilable,
               'cour_avai_select': 'checked' if this_course.cour_avilable else '',
               option_num: 'selected="selected"'}
    return render(request, 'teacher/edit_course_info.html', content)


def update_course(request):
    data = request.POST
    this_course = Course(data, tch_id=request.COOKIES['tch_id'])
    this_course.submit()
    json_return = {'status': 'SUCCESS'}
    return JsonResponse(json_return)


def add_section_view(request, id, name):
    content = {'class_manage_course': 'layui-this',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'user_type': 'university',
               'user_type_show': '教师',
               'cour_name': name}
    return render(request, 'teacher/add_section.html', content)


def edit_section_view(request, id):
    content = {'class_manage_course': 'layui-this',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'user_type': 'university',
               'user_type_show': '教师',
               'sect_obj': NepSection.objects.get(pk=id)}
    return render(request, 'teacher/edit_section.html', content)


def add_setion(request):
    # print(request.POST)
    new_section = Section(info=request.POST, tch_id=request.COOKIES['tch_id'])
    json_return = new_section.submit()
    # print('json_return:', json_return)
    return JsonResponse(json_return)


def update_section(request):
    # print(request.POST)
    edit_sect = Section(id=request.POST['sect_id'], tch_id=request.COOKIES['tch_id'])
    json_return = edit_sect.update(request.POST)
    # print('json_return', json_return)
    return JsonResponse(json_return)


def upload_file(request):
    json_return = upload.handle_upload_videos(request)
    return JsonResponse(json_return)


def reupload_file(request):
    json_return = upload.handle_reupload_videos(request)
    return JsonResponse(json_return)

def cour_image(request):
    # print(request.FILES)
    json_return = upload.handle_cour_image(request)
    return JsonResponse(json_return)

def delete_course(request):
    # print(request.POST)
    cour_obj = Course(request.POST, tch_id=request.COOKIES['tch_id'])
    json_return = cour_obj.delete()
    return JsonResponse(json_return)

def delete_section(request):
    # print(request.POST)
    sect_obj = Section(id=request.POST['sect_id'], tch_id=request.COOKIES['tch_id'])
    json_return = sect_obj.delete()
    return JsonResponse(json_return)

def learn_status_details(request, ls_id):
    content = get_ls_detail(ls_id)
    return render(request, 'teacher/stu_learn_status.html', content)

def get_index_chart_data(request):
    tch_id = request.COOKIES['tch_id']
    return JsonResponse(get_index_chart(tch_id))

def get_stu_top10_chart(request, cour_id):
    return JsonResponse(get_stu_top10(cour_id=cour_id))

def get_last_week_chart(request, cour_id):
    return JsonResponse(get_last_week(cour_id=cour_id))
