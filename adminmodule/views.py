from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth
from jobseekermodule.models import JobApplication


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def contact(request):
    return render(request, 'contact.html')


def employerhomepage(request):
    if request.user.is_authenticated and len(request.user.username) == 4:
        return render(request, 'employerhomepage.html')
    else:
        return redirect('login')


def jobseekerhomepage(request):
    if request.user.is_authenticated and len(request.user.username) == 10:
        return render(request, 'jobseekerhomepage.html')
    else:
        return redirect('login')


def about(request):
    return render(request, 'about.html')


def company(request):
    return render(request, 'company.html')


def service(request):
    return render(request, 'service.html')


def signup(request):
    return render(request, 'signup.html')


from django.contrib import messages
from django.contrib.auth.models import User, auth
import re

import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'].lower()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, 'Invalid Email Format')
            return render(request, 'signup.html')

        if not re.match(password_pattern, pass1):
            messages.error(request,
                           'Password must contain at least 8 characters, including one uppercase letter, '
                           'one lowercase letter, one digit, and one special character.')
            return render(request, 'signup.html')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        if not re.match(r'^\d{4}$|^\d{10}$', username):
            messages.error(request, 'Username must be 4 or 10 digits long')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name,
                                        last_name=last_name)
        user.save()

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')

    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            stored_email = user.email.lower()
            provided_email = request.POST.get('email', '').lower()

            if stored_email == provided_email:
                auth.login(request, user)
                if len(username) == 10:
                    return redirect('jobseekerhomepage')
                elif len(username) == 4:
                    return redirect('employerhomepage')
                else:
                    return redirect('homepage')
            else:
                messages.error(request, 'Invalid Email')
                return render(request, 'login.html')
        else:
            # Check if the username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Password')
            else:
                messages.error(request, 'Invalid Username')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'homepage.html')


def read(request):
    return render(request, 'read.html')


def password_reset(request):
    return render(request, 'password_reset.html')


def account_details(request):
    user_details = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    }
    user_role = 'Employer' if len(request.user.username) == 4 else 'Job Seeker'
    return render(request, 'account_details.html', {'user_details': user_details, 'user_role': user_role})


from django.shortcuts import render
from django.contrib import messages
from .forms import UserProfileForm


def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            contact_no = form.cleaned_data['contact_no']
            address = form.cleaned_data['address']
            print("Name:", name)
            print("Username:", username)
            print("Date of Birth:", dob)
            print("Gender:", gender)
            print("Email:", email)
            print("Contact Number:", contact_no)
            print("Address:", address)

            return render(request, '')
        else:
            messages.error(request, "There were errors in the form. Please correct them.")
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_homepage')  # Redirect to admin homepage
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'admin_login.html')  # Render admin login page with error message

    return render(request, 'admin_login.html')  # Render admin login page


# Redirect to admin login page after logout


def admin_homepage(request):
    return render(request, 'admin_homepage.html')


def admin_logout(request):
    auth.logout(request)
    return render(request, 'admin_login.html')


def admin_dashboard(request):
    # Get all users
    all_users = User.objects.all()

    # Separate users based on username length
    employers = []
    jobseekers = []
    for user in all_users:
        if len(user.username) == 4:
            employers.append(user)
        elif len(user.username) == 10:
            jobseekers.append(user)

    return render(request, 'admin_dashboard.html', {'employers': employers, 'jobseekers': jobseekers})


def delete_user(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        user.delete()
        return redirect('admin_dashboard')
    else:
        # Handle GET request, if needed
        pass


def user_application_dashboard(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'user_application_dashboard.html', {'job_applications': job_applications})


def delete_job_application(request, application_id):
    job_application = get_object_or_404(JobApplication, pk=application_id)

    if request.method == 'POST':
        job_application.delete()
        return redirect('user_application_dashboard')

    return render(request, 'confirm_delete.html', {'job_application': job_application})


def confirm_delete_application(request, application_id):
    job_application = get_object_or_404(JobApplication, pk=application_id)
    return render(request, 'confirm_delete.html', {'job_application': job_application})


def send_job_application_email(job_application):
    """
    Send an email to the user regarding the status of their job application.
    """
    subject = 'Application Accepted'
    message = 'Your job application has been accepted.'
    sender_email = 'ssaleem2409@example.com'  # Replace with your email address or use a configured email account
    recipient_email = job_application.applicant_email  # Assuming you have a field for applicant's email

    send_mail(
        'Test Subject',
        'Test message.',
        'ssaleem2409@example.com',  # Sender's email address
        ['ssaleem2409@@example.com'],  # Recipient's email address
        fail_silently=False,
    )


def accept_job_application(request, application_id):
    job_application = get_object_or_404(JobApplication, pk=application_id)

    if request.method == 'POST':
        # Mark the application as accepted (you may have a field in your model for this)
        job_application.accepted = True
        job_application.save()

        # Send an email to the user
        send_job_application_email(job_application)

        return redirect('user_application_dashboard')

    return render(request, 'confirm_accept.html', {'job_application': job_application})


def confirm_accept_application(request, application_id):
    job_application = get_object_or_404(JobApplication, pk=application_id)
    return render(request, 'confirm_accept.html', {'job_application': job_application})
