# Generated by Django 5.0.3 on 2024-04-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0011_alter_application_applicant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicant_email',
            field=models.EmailField(max_length=254),
        ),
    ]
