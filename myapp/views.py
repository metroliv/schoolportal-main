from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Category, Post, Article, Staff, UserProfile, Room
from .forms import UserSettingsForm, StaffForm, UserProfileForm
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm, UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.utils.encoding import force_bytes
from .models import UserSettings
from .forms import SubscriptionForm
from .models import Subscription 

from .models import Book
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .tasks import add

from django.db.models import Q
from student_management.models import Student
from Extracurricular.models import Events
from academic.models import Assignment, Course






def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type')  

        if user_form.is_valid():
            messages.success(request, 'Account created successfully!')
            user = user_form.save()            

            # Process according to user type
            if user_type == 'student':
                student_form = StudentForm(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
                    messages.success(request, 'Student account created successfully!')
                    return redirect('login')
                else:
                    for field, errors in student_form.errors.items():
                        for error in errors:
                            messages.error(request, f'Error in {field}: {error}')
            elif user_type == 'staff':
                staff_form = StaffForm(request.POST)
                if staff_form.is_valid():
                    staff = staff_form.save(commit=False)
                    staff.user = user
                    staff.save()
                    messages.success(request, 'Staff account created successfully!')
                    return redirect('login')
                else:
                    for field, errors in staff_form.errors.items():
                        for error in errors:
                            messages.error(request, f'Error in {field}: {error}')
            elif user_type == 'superuser':
                user.is_superuser = True
                user.is_staff = True
                user.save()
                messages.success(request, 'Superuser account created successfully!')
                return redirect('login')

    else:
        user_form = UserCreationForm()
    
    return render(request, 'register.html', {'form': user_form})
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.html"
                    context = {
                        "email": user.email,
                        'domain': request.get_host(),
                        'site_name': 'Your site name',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, context)
                    send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                messages.success(request, 'An email has been sent with instructions to reset your password.')
                return redirect('password_reset_done')
            else:
                messages.error(request, 'No user found with that email address.')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})

def help(request):
    return render(request, 'help.html')

def counter(request):
    return render(request, 'counter.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'article_list.html', {'articles': articles})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def chat_room(request, room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })

def my_model(request):
    return render(request, 'MyModel.html')

def user_settings(request):
    print("User Settings view accessed")
    try:
        settings = request.user.usersettings
    except UserSettings.DoesNotExist:
        settings = UserSettings(user=request.user)
    
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully!')
            return redirect('user_settings')
    else:
        form = UserSettingsForm(instance=settings)
    
    return render(request, 'settings/user_settings.html', {'form': form})

@login_required
def staff_list(request):
    staffs = Staff.objects.all()
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff created successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_list.html', {'staffs': staffs, 'form': form})

@login_required
def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff_detail.html', {'staff': staff})

@login_required
def staff_create(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff created successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form})

@login_required
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff updated successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_form.html', {'form': form})

@login_required
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        staff.delete()
        messages.success(request, 'Staff deleted successfully.')
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff': staff})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'profiles/profile.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'profiles/profile_edit.html', {'form': form})



def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to our newsletter.')
            return redirect('subscribe')  # Redirect to avoid resubmission
    else:
        form = SubscriptionForm()

    return render(request, 'subscribe.html', {'form': form})

@method_decorator(cache_page(60 * 15), name='dispatch')
class CachedBookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

# Example of optimized query with caching for function-based view
@cache_page(60 * 15)  # Cache for 15 minutes
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'books/book_list.html', {'books': books})

# Example of using Celery task
def my_view(request):
    result = add.delay(2, 2)
    return render(request, 'my_template.html', {'result': result})




def user_diagnostic_view(request):
    context = {
        'status': 'All systems operational',
        'user_info': {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username if request.user.is_authenticated else 'Guest',
            'email': request.user.email if request.user.is_authenticated else 'N/A',
        }
    }
    return render(request, 'user_diagnostic.html', context)


def search_main(request):
    query = request.GET.get('q', '')
    students = []
    events = []
    assignments = []
    courses = []

    if query:
        students = Student.objects.filter(name__icontains=query)
        events = Events.objects.filter(name__icontains=query)
        assignments = Assignment.objects.filter(title__icontains=query)
        courses = Course.objects.filter(title__icontains=query)

    return render(request, 'search_main.html', {
        'query': query,
        'students': students,
        'events': events,
        'assignments': assignments,
        'courses': courses,
    })

def test_view(request):
    return render(request, 'test.html', {})