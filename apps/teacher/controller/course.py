from typing import Dict
from index.models import NepCourse
from teacher.models import NepTeacher
import time


class Course:
    CourseObj = None
    data_return = {}

    def __init__(self, info: Dict, tch_id):
        self.CourseObj = NepCourse()
        self.data_return = {}
        if info.__contains__('cour_id'):
            self.CourseObj = NepCourse.objects.get(id=info['cour_id'], cour_create_tch_id=tch_id)

        try:
            # current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.CourseObj.cour_name = info['cour_name']
            #      change teacher idb
            self.CourseObj.cour_create_tch = NepTeacher.objects.get(pk=tch_id)
            self.CourseObj.cour_type = info['cour_type']
            [self.CourseObj.cour_start, self.CourseObj.cour_end] = info['cour_range'].split(' - ')
            self.CourseObj.cour_description = info['cour_description']
            self.CourseObj.cour_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.CourseObj.cour_avilable = info['cour_available']

        except Exception as ecpt:
            self.data_return['OBJ_INIT_ERROR'] = repr(ecpt)

    def submit(self):
        try:
            self.CourseObj.save()
            self.data_return['status'] = 'SUCCESS'
        except Exception as ecpt:
            self.data_return['OBJ_SUBMIT_ERROR'] = repr(ecpt)

        return self.data_return

    def delete(self):
        self.CourseObj.delete()
        self.data_return['status'] = 'SUCCESS'
        return self.data_return