from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewJobSeekerForm(UserCreationForm):
	email = forms.EmailField(max_length= 20, required=True, unique = True)
	first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    about_me = forms.CharField()
    upload_photo = forms.ImageField(upload_to='images/photo')
    upload_resume = forms.ImageField(upload_to='images/resume')
    
	

	class Meta:
		model = User
		fields = ("email", "password1", "password2", "first_name", "last_name","about_me", "upload_photo","upload_resume")

	def save(self, commit=True):
		user = super(NewJobSeekerForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class NewBusinessForm(UserCreationForm):
    email = forms.EmailField(max_length=20, required=True, unique=True)
    recruiter_firstname = forms.CharField(max_length=20, required=True)
    recruiter_lastname = forms.CharField(max_length=20, required=True)
    company_name = forms.CharField(max_length=50, required=True)
    upload_photo = forms.ImageField(upload_to='images/photo')
    upload_companyphoto = forms.ImageField(upload_to='images/companyphoto')
    about_company = forms.CharField()


	class Meta:
		model = User
		fields = ("email", "password1", "password2", "recruiter_firstname", "recruiter_lastname", "company_name", "upload_photo", "upload_companyphoto", "about_company")

	def save(self, commit=True):
		user = super(NewBusinessForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user