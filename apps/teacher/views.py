from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .controller.course import Course
from .controller.section import Section
from index.models import NepCourse
from .controller import upload


# Create your views here.

def login(request):
    return HttpResponse('login_form')


def index(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '', }
    return render(request, 'teacher/index.html', content)


def create_course(request):
    content = {'class_manage_course': '',
               'class_create_course': 'class=active-menu',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '', }
    return render(request, 'teacher/create_course.html', content)


def user_profile(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': 'class=active-menu'}
    return render(request, 'teacher/index.html', content)


def course_list(request):
    #   change teacher id
    cour_list = NepCourse.objects.filter(cour_create_tch=1)
    content = {'class_manage_course': 'class=active-menu',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'cour_list': cour_list}
    return render(request, 'teacher/manage_course.html', content)


def search_course(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': 'class=active-menu',
               'class_search_user': '',
               'class_profile': ''}
    return render(request, 'teacher/index.html', content)


def search_user(request):
    content = {'class_manage_course': '',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': 'class=active-menu',
               'class_profile': ''}
    return render(request, 'teacher/index.html', content)


def new_course(request):
    print(request.POST)
    NewCourse = Course(request.POST)
    NewCourse.submit()
    content = {'result': request.POST}
    return render(request, 'teacher/result.html', content)


def course_info(request, id):
    this_course = NepCourse.objects.get(id=id)
    cour_date = str(this_course.cour_start) + ' - ' + str(this_course.cour_end)
    option_num = 'option_' + str(this_course.cour_type)
    content = {'class_manage_course': 'class=active-menu',
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
    return render(request, 'teacher/course_info.html', content)


def update_course(request):
    data = request.POST
    print(data)
    this_course = Course(data)
    this_course.submit()
    json_return = {'status': 'SUCCESS'}
    return JsonResponse(json_return)


def add_section_view(request, id, name):
    content = {'class_manage_course': 'class=active-menu',
               'class_create_course': '',
               'class_search_course': '',
               'class_search_user': '',
               'class_profile': '',
               'user_type': 'university',
               'user_type_show': '教师',
               'cour_name': name}
    return render(request, 'teacher/add_section.html', content)


def add_setion(request):
    print(request.POST)
    NewSection = Section(request.POST)
    json_return = NewSection.submit()
    print(json_return)
    return JsonResponse(json_return)


def upload_file(request):
    print(type, id)
    print(request.POST)
    upload_path = 'media/' + request.POST['cour_id'] + '/' + request.POST['tag'] + '.mp4'
    status = upload.handle_upload_videos(file=request.FILES['file'], filename=request.POST['tag'] + '.mp4',
                                         path='static/media/' + request.POST['cour_id'] + '/')
    return JsonResponse({'status': status,
                         'path': upload_path})
