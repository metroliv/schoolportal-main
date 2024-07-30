# schoolportal/student_management/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student, Staff
from django.contrib.auth import get_user_model
from .models import  UserProfile

class StudentRegisterForm(UserCreationForm):
    student_id = forms.CharField(max_length=20)
    course = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'student_id', 'course']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
            Student.objects.create(user=user, student_id=self.cleaned_data['student_id'], course=self.cleaned_data['course'])
        return user

class StaffRegisterForm(UserCreationForm):
    staff_id = forms.CharField(max_length=20)
    department = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'staff_id', 'department']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
            Staff.objects.create(user=user, staff_id=self.cleaned_data['staff_id'], department=self.cleaned_data['department'])
        return user
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'phone_number', 'location', 'hobby', 'gender']