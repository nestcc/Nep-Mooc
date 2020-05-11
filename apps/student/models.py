from django.db import models


class NepStudent(models.Model):
    password = models.CharField(max_length=50, default='password')
    stu_name = models.CharField(max_length=45, null=True)
    stu_mobile = models.CharField(unique=True, max_length=15)
    stu_recommend_cour_info = models.CharField(max_length=30, null=True)
    stu_graduate_date = models.DateField(max_length=15, null=True)
    stu_univ = models.ForeignKey('index.NepUniversity', models.SET_NULL, null=True)
    stu_last_login_time = models.DateTimeField(null=True, default='2020-01-01 00:00:00')
    stu_last_login_ip = models.CharField(max_length=30, null=True, default='0.0.0.0')
    stu_profile = models.CharField(max_length=200, null=True)
    stu_register_time = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'nep_student'
