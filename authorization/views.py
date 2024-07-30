from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm, UserCreationForm
from django.core.mail import send_mail

from django.conf import settings
def home(request):
    return render(request, 'home.html')

def register_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add more fields as needed
        try:
            user = User.objects.create_user(username=username, password=password)
            user.profile.is_student = True  # Set student-specific attributes
            user.profile.save()
            login(request, user)
            return redirect('student_dashboard')
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'register_student.html')

def register_staff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add more fields as needed
        try:
            user = User.objects.create_user(username=username, password=password)
            user.profile.is_staff = True  # Set staff-specific attributes
            user.profile.save()
            login(request, user)
            return redirect('staff_dashboard')
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'register_staff.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.profile.is_staff:
                return redirect('staff_dashboard')
            elif user.profile.is_student:
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login1.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

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

def church_system(request):
    return render(request, 'church_system.html')

def corporate_system(request):
    return render(request, 'corporate_system.html')

def contact(request):
    return render(request, 'contact.html')
def acquire_system(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        system = request.POST.get('system')
        message = request.POST.get('message', '')

        # Optionally, you could send an email or save the data to the database
        # Example of sending an email (adjust to fit your configuration)
        subject = 'System Acquisition Request'
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        System: {system}
        Message: {message}
        """
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['support@managementportal.com'])

        # Redirect or render a confirmation page
        return render(request, 'acquire_confirmation.html', {'name': name, 'system': system})

    return render(request, 'acquire_system.html')