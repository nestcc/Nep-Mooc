from typing import Dict
from index.models import NepCourse
from teacher.models import NepTeacher
import time


class Course:
    CourseObj = NepCourse()
    submit_return = {}

    def __init__(self, info: Dict):
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

    def submit(self):
        try:
            self.CourseObj.save()
            self.submit_return['status'] = 'SUCCESS'
        except Exception as ecpt:
            self.submit_return['OBJ_SUBMIT_ERROR'] = ecpt

        return self.submit_return

    def find(self):
        pass
