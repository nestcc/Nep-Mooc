from django.db import models


class NepUniversity(models.Model):
    univ_name = models.CharField('university name', max_length=30, null=False, default='unknow')
    univ_city = models.CharField('university city', max_length=10, null=False, default='unknow')
    univ_description = models.CharField('description', max_length=100)

    class Meta:
        managed = True
        db_table = 'nep_university'


class NepCourse(models.Model):
    COURSE_TYPE = {
        ('0', '数学'),
        ('1', '化学'),
        ('2', '物理'),
        ('3', '地理'),
        ('4', '信息技术'),
        ('5', '外语'),
        ('6', '政治'),
        ('7', '历史'),
        ('8', '医学'),
        ('9', '法学'),
        ('10', '经济学')
    }

    cour_name = models.CharField(max_length=45)   #
    cour_type = models.CharField(default='unknow', max_length=10, choices=COURSE_TYPE)   #
    cour_start = models.DateTimeField(null=True)   #
    cour_end = models.DateTimeField(null=True)    #
    cour_dir = models.CharField(max_length=45, null=True)
    cour_create_tch = models.ForeignKey('teacher.NepTeacher', models.CASCADE)    #
    cour_avilable = models.BooleanField(default=True)
    cour_description = models.TextField(null=True)     #
    cour_univ = models.ForeignKey('index.NepUniversity', models.SET_NULL, null=True)   #
    cour_create_time = models.DateTimeField(null=True)  #
    cour_image = models.ImageField(null=True, height_field=92, width_field=182)

    class Meta:
        managed = True
        db_table = 'nep_course'


class NepSection(models.Model):
    sect_name = models.CharField(max_length=50)
    sect_text = models.CharField(max_length=500, null=True)
    sect_media = models.CharField(max_length=50, null=True)
    sect_cour = models.ForeignKey(NepCourse, models.CASCADE)
    sect_teacher = models.ForeignKey('teacher.NepTeacher', models.CASCADE)
    sect_tag = models.CharField(max_length=20, default='section_1-1', null=True)
    sect_create_time = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'nep_section'


class NepLearnStatus(models.Model):
    id_student = models.ForeignKey('student.NepStudent', models.CASCADE)
    id_course = models.ForeignKey(NepCourse, models.CASCADE)
    percentage = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    last_time = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'nep_learn_status'