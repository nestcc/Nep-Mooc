from index.models import NepLearnStatus, NepCourse, NepSectionStatus, NepSection
from student.models import NepStudent
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

def get_learned(cour_id, stu_id):
    # sect_status_obj = NepSectionStatus.objects.filter(course_id=cour_id, student_id=stu_id)
    sect_complete = []
    sect_start = []
    for each in NepSectionStatus.objects.filter(course_id=cour_id, student_id=stu_id):
        if each.completed:
            sect_complete.append(each.section_id)
        else:
            sect_start.append(each.section_id)
    return {'complete': sect_complete,
            'start': sect_start}

def before_learn(sect_id, stu_id):
    if NepSectionStatus.objects.filter(section_id=sect_id, student_id=stu_id).count() == 0:
        new_status = NepSectionStatus()
        new_status.section_id = sect_id
        new_status.student_id = stu_id
        new_status.course = NepSection.objects.get(pk=sect_id).sect_cour
        new_status.start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        new_status.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        new_status.save()

        cour_status = NepLearnStatus.objects.get(course=new_status.course, student_id=stu_id)
        cour_status.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        cour_status.save()

    else:
        exit_status = NepSectionStatus.objects.get(section_id=sect_id, student_id=stu_id)
        exit_status.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        exit_status.save()

        cour_status = NepLearnStatus.objects.get(course=exit_status.course, student_id=stu_id)
        cour_status.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        cour_status.save()

def finish_sect_handler(sect_id, stu_id):
    sect_status = NepSectionStatus.objects.get(section_id=sect_id, student_id=stu_id)
    cour_id = sect_status.course_id
    if not sect_status.completed:
        sect_status.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sect_status.completed = True
        sect_status.save()

        learn_status = NepLearnStatus.objects.get(student_id=stu_id, course=sect_status.course)

        finished = NepSectionStatus.objects.filter(course_id=cour_id, student_id=stu_id, completed=True).count()
        all = NepSection.objects.filter(sect_cour_id=cour_id).count()

        learn_status.percentage = int((finished/all) * 100)
        learn_status.save()

    return {'status': "SUCCESS",
            'url': '/student/course_page/' + str(cour_id) + '/'}

class LearnStatus():
    obj = None

    def __init__(self, **kwargs):
        if 'id' in kwargs.keys():
            self.obj = NepLearnStatus.objects.get(id=kwargs['id'])
        else:
            pass
