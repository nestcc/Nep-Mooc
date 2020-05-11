from django.urls import path, include
from django.contrib import admin
from apps.student import views as stuViews
from apps.teacher import views as tchViews
from apps.index import views as indexViews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', indexViews.redirect_home, name='home'),

    path('index/', include(
        [path('stu_login/', indexViews.stu_login_view),
         path('submit_stu_login/', indexViews.stu_login),
         path('tch_login/', indexViews.tch_login_view),
         path('submit_tch_login/', indexViews.tch_login),
         path('log_out/', indexViews.log_out, name='log_out')
         ]
    )),

    path('teacher/', include(
        [path('index/', tchViews.index, name='tch_index'),
         path('create_course/', tchViews.create_course, name='tch_create_course'),
         path('submit_course/', tchViews.new_course, name='submit_course'),
         path('manage_course/', tchViews.course_list, name='tch_course_list'),
         path('profile/', tchViews.user_profile, name='tch_profile'),
         path('all_course/', tchViews.search_course, name='tch_search_cour'),
         path('find_someone/', tchViews.search_user, name='tch_search_user'),
         path('edit_course_info/<int:id>', tchViews.edit_course_info),
         path('course_info/<int:id>/', tchViews.course_info, name='course_info'),
         path('update_course/', tchViews.update_course, name='update_course'),
         path('add_section/<int:id>/<str:name>/', tchViews.add_section_view, name='add_section'),
         path('edit_section_info/<int:id>/', tchViews.edit_section_view),
         path('submit_section/', tchViews.add_setion, name='submit_section'),
         path('update_section/', tchViews.update_section),
         path('upload/', tchViews.upload_file),
         path('reupload/', tchViews.reupload_file),
         path('cour_image/', tchViews.cour_image),
         path('learn_detail/<int:ls_id>/', tchViews.learn_status_details),

         path('delete_course/', tchViews.delete_course),
         path('delete_section/', tchViews.delete_section),

         path('get_learn_list/<int:id>/', tchViews.get_stu_by_cour, name='get_learn_list'),
         path('get_section_list/<int:id>/', tchViews.get_sect_by_cour, name='get_section_list'),

         path('get_index_chart/', tchViews.get_index_chart_data),
         path('get_stu_top10_chart/<int:cour_id>/', tchViews.get_stu_top10_chart),
         path('get_last_week_chart/<int:cour_id>/', tchViews.get_last_week_chart)
         ]
    )),

    path('student/', include(
        [path('index/', stuViews.index, name='stu_index'),
         path('my_course/<int:page>/', stuViews.my_course, name='my_course'),
         path('search_course/<int:page>/', stuViews.search_course, name='stu_search_course'),
         path('search_course/<int:page>/<str:info>/', stuViews.search_course_by_info),
         path('search_user/', stuViews.search_user, name='stu_search_user'),
         path('profile/', stuViews.profile, name='stu_profile'),
         path('show_cour_info/<int:id>/', stuViews.show_cour_info),
         path('join_course/', stuViews.join_course),
         path('quit_course/', stuViews.quit_course),
         path('course_page/<int:id>/', stuViews.course_page),
         path('learn/<int:sect_id>/', stuViews.learn_view, name='stu_learn'),
         path('show_cour_detail/<int:id>/', stuViews.show_cour_detail),

         path('get_learned_sect/', stuViews.get_learned_sect),
         path('finished/', stuViews.finish_sect),
         path('get_recommend/', stuViews.get_recommend)
         ]
    )),
]
