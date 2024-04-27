from django.db import models


# Create your models here.
class JobDetails(models.Model):
    work_title = models.CharField(max_length=255)
    salary_offered = models.CharField(max_length=255)
    JOB_TYPES = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    benefits = models.TextField()
    education = models.CharField(max_length=255)
    work_location = models.CharField(max_length=255)
    required_skills = models.TextField()
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.work_title


class Application(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    job_applied_for = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name}'s application for {self.job_applied_for}"