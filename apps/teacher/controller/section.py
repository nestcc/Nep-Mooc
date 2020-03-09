from index.models import  NepCourse, NepSection
from teacher.models import NepTeacher
from typing import Dict
import time

class Section():
    SectionObj = NepSection()
    submit_return = {}

    def __init__(self, info: Dict):
        if info.__contains__('id'):
            self.SectionObj = NepSection.objects.get(id = info['id'])

        else:
            try:
                self.SectionObj.sect_cour = NepCourse.objects.get(id = info['sect_cour'])
                self.SectionObj.sect_teacher = NepTeacher.objects.get(id = info['sect_teacher'])
                self.SectionObj.sect_name = info['sect_name']
                self.SectionObj.sect_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                self.SectionObj.sect_tag = info['sect_tag']
                self.SectionObj.sect_text = info['sect_text']
                self.SectionObj.sect_media = info['sect_media']

            except Exception as ecpt:
                self.submit_return['OBJ_INIT_ERROR'] = str(ecpt)

    def submit(self):
        try:
            self.SectionObj.save()
            self.submit_return['status'] = 'SUCCESS'
        except Exception as ecpt:
            self.submit_return['OBJ_SUBMIT_ERROR'] = ecpt

        return self.submit_return