
from django.urls import path
from . import views

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:id>/', views.event_detail, name='event_detail'),
]
