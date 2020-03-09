from teacher.models import NepTeacher


class Register():
    newTeacher = NepTeacher()

    def __init__(self, password: str, name: str, mobile: str):
        self.newTeacher.tch_name = name
        self.newTeacher.password = password
        self.newTeacher.tch_mobile = mobile

    def register(self):
        self.newTeacher.save()
