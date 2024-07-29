from django.contrib import admin
from .models import Course, Class, Assignment, Grade, Attendance

admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(Attendance)
