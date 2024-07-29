from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Assignment, Grade, Attendance
from student_management.models import Student  # Import Student model
from .forms import CourseForm, AssignmentForm, GradeForm, AttendanceForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'academic/course_list.html', {'courses': courses})

def assignment_detail(request, course_id):
    assignments = Assignment.objects.filter(course_id=course_id)
    return render(request, 'academic/assignment_detail.html', {'assignments': assignments})

def grades_list(request):
    try:
        student = get_object_or_404(Student, admission_number=request.user.username)
        grades = Grade.objects.filter(student=student)
    except Student.DoesNotExist:
        grades = []
        message = "No grades found for this student."
    else:
        message = None

    return render(request, 'academic/grades_list.html', {'grades': grades, 'message': message})

@login_required
def attendance_report(request):
    try:
        student = get_object_or_404(Student, admission_number=request.user.username)
        attendance = Attendance.objects.filter(student=student)
        message = None if attendance else "No attendance records found for this student."
    except Student.DoesNotExist:
        attendance = []
        message = "No student found with this admission number."

    return render(request, 'academic/attendance_report.html', {
        'attendance': attendance,
        'message': message,
    })

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'academic/add_course.html', {'form': form})

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_detail', course_id=form.cleaned_data['course'].id)
    else:
        form = AssignmentForm()
    return render(request, 'academic/add_assignment.html', {'form': form})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades_list')
    else:
        form = GradeForm()
    return render(request, 'academic/add_grade.html', {'form': form})

def add_attendance(request):
    try:
        student = get_object_or_404(Student, admission_number=request.user.username)
    except Student.DoesNotExist:
        return render(request, 'academic/error.html', {'message': "No student found with this admission number."})

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = student  # Assign the retrieved student
            attendance.save()
            return redirect('attendance_report')
    else:
        form = AttendanceForm()

    return render(request, 'academic/add_attendance.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    courses = Course.objects.filter(name__icontains=query) if query else []
    assignments = Assignment.objects.filter(title__icontains=query) if query else []
    return render(request, 'academic/search_results.html', {'query': query, 'courses': courses, 'assignments': assignments})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Add subscription logic here
        return render(request, 'academic/thank_you.html', {'email': email})
    return redirect('/')
