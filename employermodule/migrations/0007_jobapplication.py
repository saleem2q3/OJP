# Generated by Django 5.0.3 on 2024-03-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0006_remove_job_applicants_delete_jobapplication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('job_details', models.TextField()),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('cover_letter', models.TextField()),
            ],
        ),
    ]
