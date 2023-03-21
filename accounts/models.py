from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)


class Jobseeker(models.Model):
    User.is_jobseeker = True
    email = models.EmailField(max_length= 20, unique = True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    about_me = models.TextField()
    upload_photo = models.ImageField(upload_to='images/photo')
    upload_resume = models.ImageField(upload_to='images/resume')
    


class Business(models.Model):
    User.is_business = True
    email = models.EmailField(max_length=20, unique=True)
    recruiter_firstname = models.CharField(max_length=20)
    recruiter_lastname = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    upload_photo = models.ImageField(upload_to='images/photo')
    upload_companyphoto = models.ImageField(upload_to='images/companyphoto')
    about_company = models.TextField()

