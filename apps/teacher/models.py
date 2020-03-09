from django.db import models


class NepTeacher(models.Model):
    password = models.CharField('password', max_length=50, default='password')
    tch_name = models.CharField('teacher name', null=True, max_length=10)
    # user_type = models.IntegerField('user type, 0: tch, 1: stu', null=False, default=1)
    tch_mobile = models.CharField('mobile', unique=True, max_length=15)
    tch_register_time = models.DateTimeField('register time', null=True, default='2020-01-01 00:00:00')
    tch_last_login_time = models.DateTimeField('last log in time', null=True, default='2020-01-01 00:00:00')
    tch_last_login_ip = models.CharField('last log in ip', max_length=30, null=True)
    tch_profile = models.CharField(max_length=200, null=True)
    tch_univ = models.ForeignKey('index.NepUniversity', on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'nep_teacher'
