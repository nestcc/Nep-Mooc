from django.db import models


class NepUniversity(models.Model):
    univ_name = models.CharField('university name', max_length=30, default='unknow')
    univ_city = models.CharField('university city', max_length=10, default='unknow')
    univ_description = models.CharField('description', max_length=100, null=True)

    class Meta:
        managed = True
        db_table = 'nep_university'


class NepCourse(models.Model):
    COURSE_TYPE = {
        ('0', '哲学'),
        ('1', '经济学'),
        ('2', '法学'),
        ('3', '教育学'),
        ('4', '文学'),
        ('5', '历史学'),
        ('6', '理学'),
        ('7', '工学'),
        ('8', '农学'),
        ('9', '医学'),
        ('10', '管理学'),
        ('11', '艺术学'),
        ('12', '军事学'),
        ('13', '其他')
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
    cour_image = models.ImageField(null=True, default='default.png')

    class Meta:
        managed = True
        db_table = 'nep_course'


class NepSection(models.Model):
    sect_name = models.CharField(max_length=50)
    sect_text = models.CharField(max_length=500, null=True)
    sect_media = models.CharField(max_length=200, null=True)
    sect_cour = models.ForeignKey(NepCourse, models.CASCADE)
    sect_teacher = models.ForeignKey('teacher.NepTeacher', models.CASCADE)
    sect_tag = models.CharField(max_length=20, default='1-1')
    sect_create_time = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'nep_section'


class NepLearnStatus(models.Model):
    student = models.ForeignKey('student.NepStudent', models.CASCADE)
    course = models.ForeignKey(NepCourse, models.CASCADE)
    percentage = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    last_time = models.DateTimeField(null=True)
    learn_frequency = models.IntegerField(default=0, null=True)

    class Meta:
        managed = True
        db_table = 'nep_learn_status'


class NepSectionStatus(models.Model):
    student = models.ForeignKey('student.NepStudent', models.CASCADE)
    course = models.ForeignKey(NepCourse, models.CASCADE)
    section = models.ForeignKey(NepSection, models.CASCADE)
    start_time = models.DateTimeField(null=True)
    last_time = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    view_time = models.TimeField(null=True)

    class Meta:
        managed = True
        db_table = 'nep_section_status'
