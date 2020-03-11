from index.models import NepLearnStatus, NepCourse
from student.models import NepStudent
from typing import Dict
import time


def new_status(id_stu, id_cour):
    new_item = NepLearnStatus()
    dual_status = NepLearnStatus.objects.filter(course_id=id_cour, student_id=id_stu)

    print(dual_status.count())
    if dual_status.count() != 0:
        return {'status': 'FAIL',
                'error': 'DUAL'}
    else:
        new_item.course = NepCourse.objects.get(pk=id_cour)
        new_item.student = NepStudent.objects.get(pk=id_stu)
        new_item.percentage = 0
        new_item.start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        try:
            new_item.save()
            return {'status': 'SUCCESS'}
        except Exception as excp:
            return {'status': 'FAIL',
                    'error': repr(excp)}


class LearnStatus():
    obj = None

    def __init__(self, **kwargs):
        if 'id' in kwargs.keys():
            self.obj = NepLearnStatus.objects.get(id=kwargs['id'])
        else:
            pass
