# Generated by Django 5.0.3 on 2024-04-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0009_jobdetails_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('job_applied_for', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
