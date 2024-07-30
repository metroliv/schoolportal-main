from django.contrib import admin
from .models import CustomUser, Student, Staff

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (StudentInline, StaffInline)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Staff)
