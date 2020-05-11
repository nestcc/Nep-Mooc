from index.models import NepLearnStatus, NepSection, NepSectionStatus, NepCourse
from student.models import NepStudent
from teacher.models import NepTeacher
import datetime


def get_learn_list(course_id, limit=5, page=1):
    status_query = NepLearnStatus.objects.filter(course_id=course_id)
    data = []
    status = 0
    count = status_query.count()

    for each_status in status_query[(page - 1) * limit: page * limit]:
        # print(NepStudent.objects.get(pk=each_status.student_id))
        data.append({
            'id': each_status.id,
            'name': each_status.student.stu_name,
            'start': each_status.start_time,
            'last': each_status.last_time,
            'number': str(each_status.percentage) + '%',
        })

    return {'code': status,
            'count': count,
            'msg': '',
            'data': data}


def get_section_list(course_id, limit=5, page=1):
    sect_query = NepSection.objects.filter(sect_cour_id=course_id).order_by('sect_tag')
    data = []
    status = 0
    count = sect_query.count()

    for each_item in sect_query[(page - 1) * limit: page * limit]:
        data.append({
            'id': each_item.id,
            'sect_name': each_item.sect_name,
            'sect_tag': each_item.sect_tag,
            'create_time': each_item.sect_create_time
        })

    return {'code': status,
            'count': count,
            'msg': '',
            'data': data}


def get_ls_detail(ls_id):
    ls_obj = NepLearnStatus.objects.get(pk=ls_id)

    content = {
        'id': ls_obj.id,
        'stu_name': ls_obj.student.stu_name,
        'stu_univ': ls_obj.student.stu_univ,
        'stu_profile': ls_obj.student.stu_profile,
        'stu_mobile': ls_obj.student.stu_mobile,
        'stu_register_time': ls_obj.student.stu_register_time,
        'start_time': ls_obj.start_time,
        'last_time': ls_obj.last_time,
        'percentage': ls_obj.percentage,
        'finished': NepSectionStatus.objects.filter(course=ls_obj.course, student=ls_obj.student, completed=True),
        'learning': NepSectionStatus.objects.filter(course=ls_obj.course, student=ls_obj.student, completed=False)
    }
    return content


def get_index_chart(tch_id=1):
    cour_obj = NepCourse.objects.filter(cour_create_tch_id=tch_id)
    x_data = []
    y_data = []
    for each_cour in cour_obj:
        if each_cour.get_cour_type_display() in x_data:
            y_data[x_data.index(each_cour.get_cour_type_display())] += 1
        else:
            x_data.append(each_cour.get_cour_type_display())
            y_data.append(1)

    return {'x_data': x_data,
            'y_data': y_data}

def get_stu_top10(cour_id):
    ls_obj = NepLearnStatus.objects.filter(course_id=cour_id).order_by('-percentage')
    x_data, y_data = [], []

    for each_ls in ls_obj[0:10]:
        x_data.append(each_ls.student.stu_name)
        y_data.append(NepSectionStatus.objects.filter(course_id=cour_id, student=each_ls.student).count())

    return {'x_data': x_data,
            'y_data': y_data}

def get_last_week(cour_id):
    # print(datetime.date.today() - datetime.timedelta(days=6))
    ss_obj = NepSectionStatus.objects.filter(course_id=cour_id, last_time__gte=datetime.date.today()-datetime.timedelta(days=6))
    x_data, y_data = [], []
    stu_top10 = {}
    for each_ss in ss_obj[0:5]:
        if each_ss.student.stu_name not in x_data:

            x_data.append(each_ss.student.stu_name)
            y_data.append(1)
        else:
            y_data[x_data.index(each_ss.student.stu_name)] += 1

    return {'x_data': x_data,
            'y_data': y_data}
