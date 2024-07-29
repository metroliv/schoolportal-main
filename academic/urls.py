from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.assignment_detail, name='assignment_detail'),
    path('grades/', views.grades_list, name='grades_list'),
    path('attendance/', views.attendance_report, name='attendance_report'),
    path('add-course/', views.add_course, name='add_course'),
    path('add-assignment/', views.add_assignment, name='add_assignment'),
    path('add-grade/', views.add_grade, name='add_grade'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('search/', views.search, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
