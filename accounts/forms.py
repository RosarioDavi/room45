from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from accounts.models import Jobseeker, Business, User

class JobSeekerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_jobseeker = True
        user.save()
        return user

class BusinessSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
    
    def save(self):
        user = super().save(commit=False)
        user.is_business = True
        user.save()
        return user