# Generated by Django 2.2.5 on 2020-01-02 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NepStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='password', max_length=50)),
                ('stu_name', models.CharField(max_length=45, null=True)),
                ('stu_mobile', models.CharField(max_length=15, unique=True)),
                ('stu_cour_info', models.CharField(max_length=30, null=True)),
                ('stu_last_login_time', models.DateTimeField(default='2020-01-01 00:00:00', null=True)),
                ('stu_last_login_ip', models.CharField(default='0.0.0.0', max_length=30, null=True)),
                ('stu_profile', models.CharField(max_length=200, null=True)),
                ('stu_register_time', models.DateTimeField(null=True)),
                ('stu_univ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.NepUniversity')),
            ],
            options={
                'db_table': 'nep_student',
                'managed': True,
            },
        ),
    ]
