from django import forms
from .models import Student, Mark



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'phone', 'location', 'hobby', 'gender', 'picture']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("A student with this email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Student.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A student with this phone number already exists.")
        return phone


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['subject', 'marks_obtained']

class AddMarksForm(forms.Form):
    subjects = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), help_text='Enter subjects and marks in the format: Subject: Marks')

    def clean_marks_obtained(self):
        marks = self.cleaned_data.get('marks_obtained')
        if marks < 0 or marks > 100:
            raise forms.ValidationError("Marks should be between 0 and 100.")
        return marks

class PictureForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['picture']