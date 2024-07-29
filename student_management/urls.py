from django.urls import path
from . import views
from .views import (
    student_list,
    student_detail,
    student_create,
    student_update,
    student_delete,   
    studentid,
    
)

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('students/create/', student_create, name='student_create'),
    path('students/<int:pk>/update/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
    path('students/<int:student_id>/enter_marks/', views.enter_marks, name='enter_marks'),
    path('students/<int:student_id>/transcript/', views.view_transcript, name='view_transcript'),
    path('students/<int:student_id>/generate_id/', studentid, name='studentid'),
]
