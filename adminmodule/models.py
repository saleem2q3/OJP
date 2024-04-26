from django.db import models

# Create your models here.
from django.db import models


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    dob = models.DateField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username
