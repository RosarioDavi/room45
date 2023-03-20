from django.db import models

class JobSeeker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    about_me = models.TextField()
    email = models.CharField(max_length=30, unique=True)
    upload_photo = models.ImageField(upload_to='images/photo')
    upload_resume = models.ImageField(upload_to='images/resume')

    def __str__(self):
        return self.email
    

    
class Business(models.Model):
    company_name = models.CharField(max_length=50)
    recruiter_firstname = models.CharField(max_length=20)
    recruiter_lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    upload_photo = models.ImageField(upload_to='images/photo')
    upload_companyphoto = models.ImageField(upload_to='images/companyphoto')
    about_company = models.TextField()
    
    def __str__(self):
        return self.email
