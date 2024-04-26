from employermodule.models import JobDetails
from django.shortcuts import render


def viewjobs(request):
    return render(request, 'jobseekermodule/viewjobs.html')


def job_details_list(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'jobseekermodule/viewjobs.html', {'job_details_list': job_details_list})


def job_application_list(request):
    jobs = Job.objects.all()  # Assuming you're fetching a list of jobs
    context = {'jobs': jobs}
    return render(request, 'jobseekermodule/job_application_list.html', context)


def job_applications(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'job_applications.html', {'job_applications': job_applications})


def submit_application(request, job_id):
    job = JobDetails.objects.get(pk=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the job application to the database
            form.save()
            return redirect('jobseekerhomepage')
    else:
        form = JobApplicationForm(initial={'job_details': job.work_title})

    return render(request, 'submit_application.html', {'form': form})
