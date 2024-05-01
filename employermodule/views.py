from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from pyexpat.errors import messages
from django.contrib import messages
from django.core.mail import send_mail

from jobseekermodule.views import send_email
from .models import *
from jobseekermodule.models import JobApplication
from employermodule.models import Application


# Create your views here.
def jobpost(request):
    return render(request, 'employermodule/jobpost.html')


def employerlist(request):
    return render(request, 'employermodule/employerlist.html')


def add_job_details(request):
    if request.method == 'POST':
        work_title = request.POST.get('workTitle')
        salary_offered = request.POST.get('salaryOffered')
        job_type = request.POST.get('jobType')
        benefits = request.POST.get('benefits')
        education = request.POST.get('education')
        work_location = request.POST.get('workLocation')
        required_skills = request.POST.get('requiredSkills')
        experience = request.POST.get('experience')

        job_details = JobDetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            benefits=benefits,
            education=education,
            work_location=work_location,
            required_skills=required_skills,
            experience=experience,
        )
        job_details.save()
        return render(request, 'employermodule/datainserted.html')
    return render(request, 'employeerhomepage/jobpost.html')


def view_job_details(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'employermodule/view_job_details.html', {'job_details_list': job_details_list})


def edit_job_details(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        job_details.work_title = request.POST.get('workTitle')
        job_details.salary_offered = request.POST.get('salaryOffered')
        job_details.job_type = request.POST.get('jobType')
        job_details.benefits = request.POST.get('benefits')
        job_details.education = request.POST.get('education')
        job_details.work_location = request.POST.get('workLocation')
        job_details.required_skills = request.POST.get('requiredSkills')
        job_details.experience = request.POST.get('experience')
        job_details.save()
        return redirect('employermodule:view_job_details')
    return render(request, 'employermodule/edit_job_details.html', {'job_details': job_details})


def delete_job_details(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        job_details.delete()
        return redirect('employermodule:view_job_details')
    return render(request, 'employermodule/delete_job_details.html', {'job_details': job_details})


def job_applications(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'employermodule/employerlist.html', {'job_applications': job_applications})


from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from jobseekermodule.models import JobApplication
from jobseekermodule.forms import JobApplicationForm


def approve_application(request, application_id):
    application = JobApplication.objects.get(pk=application_id)
    application.status = 'approved'
    application.save()
    approve_notification(request, application)  # Pass the application instance
    return redirect('employermodule:job_applications')


def approve_notification(request, application):
    applicant_name = application.name
    send_mail(
        'Congratulations!',
        f'Hi {applicant_name},\n\nYour job application has been approved.\n\nBest Regards,\nONLINEJOBPORTAL',
        'ssaleem2409@gmail.com',  # Replace with your email address
        [application.email],  # Send email to the applicant
        fail_silently=False,
    )


def rejection_notification(request, application):
    applicant_name = application.name
    messages.error(request, f'Sorry {applicant_name}, your application has been rejected.')
    send_mail(
        'Job Application Rejected',
        f'Hi {applicant_name},\n\nWe regret to inform you that your job application has been rejected.\n\nBest Regards,\nONLINEJOBPORTAL',
        'ssaleem2409@gmail.com',  # Replace with your email address
        [application.email],  # Send email to the applicant
        fail_silently=False,
    )


def reject_application(request, application_id):
    application = JobApplication.objects.get(pk=application_id)
    application.status = 'rejected'
    application.save()
    rejection_notification(request, application)  # Pass the application instance
    return redirect('employermodule:job_applications')


def job_application_list(request):
    job_applications = JobApplication.objects.all()
    context = {
        'job_applications': job_applications
    }
    return render(request, 'employermodule/job_application_list.html', context)
