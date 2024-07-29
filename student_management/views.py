from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Mark, Transcript
from .forms import StudentForm, MarkForm, AddMarksForm, PictureForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
import pdfkit
import uuid
import os
import base64




@login_required
def student_list(request):
    query = request.GET.get('search', '')
    students = Student.objects.filter(name__icontains=query)

    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(list(students.values('id', 'name')), safe=False)

    return render(request, 'student_list.html', {'students': students, 'query': query})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})



@login_required
def enter_marks(request, student_id):
    students = Student.objects.all()
    subjects = request.POST.getlist('subjects') if request.method == "POST" else []

    if request.method == "POST":
        total_marks = 0
        for student in students:
            for subject in subjects:
                mark_value = request.POST.get(f'mark_{student.id}_{subject}')
                if mark_value:
                    mark = Mark(student=student, subject=subject, marks_obtained=float(mark_value))
                    mark.save()
                    total_marks += float(mark_value)
            # Update or create a transcript
            transcript, created = Transcript.objects.get_or_create(student=student)
            transcript.total_marks = total_marks
            transcript.save()
        
        return redirect('view_transcript', student_id=student_id)

    return render(request, 'enter_marks.html', {'students': students, 'subjects': subjects})

@login_required
def view_transcript(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    transcript = Transcript.objects.filter(student=student).first()
    marks = Mark.objects.filter(student=student)

    return render(request, 'view_transcript.html', {
        'student': student,
        'transcript': transcript,
        'marks': marks,
    })







@login_required
def studentid(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

        html_content = render_to_string('studentid_template.html', {
            'name': student.name,
            'phone': student.phone,
            'admission_number': student.admission_number,
            'serial_number': student.serial_number,
            'picture_url': student.picture.url if student.picture else None
        })

        config_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=config_path)

        options = {
            'enable-local-file-access': None,
        }

        pdf = pdfkit.from_string(html_content, False, configuration=config, options=options)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{student.name}_{student.admission_number}.pdf"'
        return response
    else:
        form = PictureForm(instance=student)
        return render(request, 'confirm_studentid.html', {'student': student, 'form': form})
