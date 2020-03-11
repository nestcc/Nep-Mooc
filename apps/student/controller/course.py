from typing import Dict
from index.models import NepCourse
from teacher.models import NepTeacher
import time


class Course:
    CourseObj = None
    submit_return = {}

    def __init__(self, **kwargs):
        if 'id' in kwargs.keys():
            self.CourseObj = NepCourse.objects.get(id=kwargs['id'])
        else:
            pass

    def find(self, info: Dict):
        if info.__contains__('cour_id'):
            print(info['cour_id'])
            self.CourseObj = NepCourse.objects.get(id=info['cour_id'])

        try:
            # current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.CourseObj.cour_name = info['cour_name']
            #      change teacher idb
            self.CourseObj.cour_create_tch = NepTeacher.objects.get(pk=1)
            self.CourseObj.cour_type = info['cour_type']
            [self.CourseObj.cour_start, self.CourseObj.cour_end] = info['cour_range'].split(' - ')
            self.CourseObj.cour_description = info['cour_description']
            self.CourseObj.cour_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        except Exception as ecpt:
            self.submit_return['OBJ_INIT_ERROR'] = ecpt

    def get_item_number(self):
        return NepCourse.objects.count()

    def all_course(self, **kwargs):
        number, page = kwargs.get('number'), kwargs.get('page')
        if number == None:
            return NepCourse.objects.all()
        else:
            return NepCourse.objects.all()[(page - 1) * number: page * number]

    def get_cour_info(self, **kwargs):
        if 'id' in kwargs.keys():
            self.CourseObj = NepCourse.objects.get(id=kwargs['id'])
        return {'id': self.CourseObj.id,
                'cour_name': self.CourseObj.cour_name,
                'cour_type': self.CourseObj.get_cour_type_display(),
                'cour_schedule': str(self.CourseObj.cour_start) + ' - ' + str(self.CourseObj.cour_end),
                'cour_description': self.CourseObj.cour_description,
                'cour_tch': self.CourseObj.cour_create_tch.tch_name}
