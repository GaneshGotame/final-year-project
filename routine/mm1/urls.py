from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('timetable_generation/', views.timetable, name='timetable'),
    path('add_room/', views.add_room, name='addroom'),
    path('add_instructor/', views.add_instructor, name='addinstructor'),
    path('instructor_list/', views.inst_list_view, name='editinstructor'),
    path('add_meetingtime/', views.add_meeting_time, name='addmeetingtime'),
    path('meetingtime_list/', views.meeting_list_view, name='editmeetingtime'),
    path('add_course/', views.add_course, name='addcourse'),
    path('course_list/', views.course_list_view, name='editcourse'),
    path('add_semester/', views.add_semester, name='addsemester'),
    path('delete_meetingtime/<str:pk>/', views.delete_meeting_time, name='deletemeetingtime'),
    path('delete_course/<str:pk>/', views.delete_course, name='deletecourse'),
    path('delete_instructor/<int:pk>/', views.delete_instructor, name='deleteinstructor'),
    path('room_list/', views.room_list, name='editrooms'),
    path('delete_room/<int:pk>/', views.delete_room, name='deleteroom'),
    path('semester_list/', views.semester_list, name='editsemester'),
    path('delete_semester/<int:pk>/', views.delete_semester, name='deletesemester'),
    path('add_select_semester/', views.add_select_semester, name='addselectsemester'),
    path('select_semester_list/', views.select_semester_list, name='editselectsemester'),
    path('delete_select_semester/<str:pk>/', views.delete_select_semester, name='deleteselectsemester'),

]
