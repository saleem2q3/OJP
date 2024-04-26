from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'name', 'username', 'dob', 'gender', 'email', 'contact', 'address']

    def clean_username(self):
        username = self.cleaned_data['username']
        # Validate that username contains only alphanumeric characters
        if not username.isalnum():
            raise forms.ValidationError("Username should contain only alphanumeric characters.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        # Validate email format
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Please provide a valid Gmail address.")
        return email

    def clean_contact(self):
        contact = self.cleaned_data['contact']
        # Validate that contact contains only numerical characters
        if not contact.isdigit():
            raise forms.ValidationError("Contact should contain only numerical characters.")
        return contact

    def clean_address(self):
        address = self.cleaned_data['address']
        # Validate that address contains only alphabetical characters
        if not address.replace(" ", "").isalpha():
            raise forms.ValidationError("Address should contain only alphabetical characters.")
        return address
