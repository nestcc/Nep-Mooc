from index.models import NepCourse, NepSection
from teacher.models import NepTeacher
from typing import Dict
import time


class Section():
    SectionObj = None
    data_return = {}

    def __init__(self, **kwargs):
        self.SectionObj = NepSection()
        self.data_return = {}
        if 'info' in kwargs.keys():
            if kwargs['info']['sect_name'] == '':
                self.data_return['OBJ_INIT_ERROR'] = 'EMPTY SECT_NAME'
            else:
                try:
                    self.SectionObj.sect_cour = NepCourse.objects.get(id=kwargs['info']['sect_cour'])
                    self.SectionObj.sect_teacher = NepTeacher.objects.get(id=kwargs['tch_id'])
                    self.SectionObj.sect_name = kwargs['info']['sect_name']
                    self.SectionObj.sect_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    self.SectionObj.sect_tag = kwargs['info']['sect_tag']
                    self.SectionObj.sect_text = kwargs['info']['sect_text']
                    self.SectionObj.sect_media = kwargs['info']['sect_media'] if 'sect_media' in kwargs['info'] else ''

                except Exception as ecpt:
                    self.data_return['OBJ_INIT_ERROR'] = repr(ecpt)

        elif 'id' in kwargs.keys():
            self.SectionObj = NepSection.objects.get(id=kwargs['id'], sect_teacher_id=kwargs['tch_id'])
        else:
            pass

    def submit(self):
        if 'OBJ_INIT_ERROR' in self.data_return.keys():
            self.data_return['status'] = 'FAIL'

        elif self.SectionObj.sect_name == '' or self.SectionObj.sect_tag == '':
            self.data_return['status'] = 'FAIL'
            self.data_return['error'] = 'None Type'
            return self.data_return
        else:
            try:
                self.SectionObj.save()
                self.data_return['status'] = 'SUCCESS'
            except Exception as ecpt:
                self.data_return['OBJ_SUBMIT_ERROR'] = repr(ecpt)

        return self.data_return

    def find_by_course(self, cour_id):
        try:
            section_list = NepSection.objects.filter(sect_cour=cour_id)
            self.data_return['section_list'] = section_list
            self.data_return['count'] = section_list.count()
        except Exception as ecpt:
            self.data_return['error'] = repr(ecpt)
        return self.data_return

    def update(self, info: Dict):
        try:
            self.SectionObj.sect_name = info['sect_name']
            self.SectionObj.sect_tag = info['sect_tag']
            self.SectionObj.sect_text = info['sect_text']

            self.SectionObj.save()
            self.data_return['status'] = 'SUCCESS'
        except Exception as ecpt:
            self.data_return['UPDATE_ERROR'] = repr(ecpt)
            self.data_return['status'] = 'FAIL'

        return self.data_return


    def delete(self):
        cour_id = str(self.SectionObj.sect_cour_id)
        self.SectionObj.delete()

        self.data_return['status'] = 'SUCCESS'
        self.data_return['url'] = '/teacher/course_info/' + cour_id + '/'

        return self.data_return
