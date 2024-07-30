from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/staff/', views.register_staff, name='register_staff'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
    path('system/church/', views.church_system, name='church_system'),
    path('system/corporate/', views.corporate_system, name='corporate_system'),
    path('contact/', views.contact, name='contact')
    path('acquire/', views.acquire_system, name='acquire_system'),  # New URL pattern
]
