from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'job_details', 'resume', 'profile_image', 'cover_letter', 'personal_information', 'work_history', 'portfolio', 'additional_documents']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'job_details': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'personal_information': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'work_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'portfolio': forms.FileInput(attrs={'class': 'form-control-file'}),
            'additional_documents': forms.FileInput(attrs={'class': 'form-control-file'}),
        }