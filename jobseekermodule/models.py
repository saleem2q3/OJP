from django.db import models

# Create your models here.
# models.py
from django.db import models


class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job_details = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # New field for profile image
    cover_letter = models.TextField(blank=True)  # Field for cover letter
    personal_information = models.TextField(blank=True)  # Field for personal information
    work_history = models.TextField(blank=True)  # Field for work history
    portfolio = models.FileField(upload_to='portfolio/', null=True, blank=True)  # Field for portfolio
    additional_documents = models.FileField(upload_to='additional_documents/', null=True, blank=True)  # Field for additional documents

    def __str__(self):
        return self.name


from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    requirements = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
