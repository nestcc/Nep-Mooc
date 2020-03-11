from django.urls import path, include
from django.contrib import admin
from apps.student import views as stuViews
from apps.teacher import views as tchViews
from apps.index import views as indexViews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', indexViews.redirect_home, name='home'),

    path('teacher/', include(
        [path('login/', tchViews.login, name='tch_login'),
         path('index/', tchViews.index, name='tch_index'),
         path('create_course/', tchViews.create_course, name='tch_create_course'),
         path('submit_course/', tchViews.new_course, name='submit_course'),
         path('manage_course/', tchViews.course_list, name='course_list'),
         path('profile/', tchViews.user_profile, name='tch_profile'),
         path('all_course/', tchViews.search_course, name='tch_search_cour'),
         path('find_someone/', tchViews.search_user, name='tch_search_user'),
         path('course_info/<int:id>', tchViews.course_info),
         path('update_course/', tchViews.update_course, name='update_course'),
         path('cour_section/<int:id>/<str:name>/', tchViews.add_section_view, name='add_section_view'),
         path('add_section/', tchViews.add_setion, name='add_section'),
         path('upload/', tchViews.upload_file)
         ]
    )),

    path('student/', include(
        [path('index/', stuViews.index, name='stu_index'),
         path('my_course/', stuViews.my_course, name='my_course'),
         path('search_course/<int:page>/', stuViews.search_course, name='stu_search_course'),
         path('search_user/', stuViews.search_user, name='stu_search_user'),
         path('profile/', stuViews.profile, name='stu_profile'),
         path('play_video/', stuViews.play_videos, name='stu_play_videos'),
         path('show_cour_info/<int:id>/', stuViews.show_cour_info),
         path('join_course/', stuViews.join_course)
         ]
    )),

    path('index/', include(
        [path('login/', indexViews.login),
         path('register/', indexViews.register),
         path('tch_login/', indexViews.tch_login),
         path('tch_register/', indexViews.tch_register)]
    ))
]
