from student.models import NepStudent
from teacher.models import NepTeacher


def stu_login_by_mobile(stu_mobile, stu_pwd):
    stu_obj = NepStudent.objects.filter(stu_mobile=stu_mobile, password=stu_pwd)
    if stu_obj.count() == 0:
        return {'status': 'INFO_ERROR'}
    else:
        return {'status': 'SUCCESS',
                'stu_id': stu_obj[0].id}


def tch_login_by_mobile(tch_mobile, tch_pwd):
    tch_obj = NepTeacher.objects.filter(tch_mobile=tch_mobile, password=tch_pwd)
    if tch_obj.count() == 0:
        return {'status': 'INFO_ERROR'}
    else:
        return {'status': 'SUCCESS',
                'tch_id': tch_obj[0].id}
