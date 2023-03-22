from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User, Jobseeker, Business
from accounts.forms import JobSeekerSignUpForm, BusinessSignUpForm

# Create your views here.
class HomeView(ListView):
    model = User
    template_name = "registration/home.html"

class SignupView(ListView):
    model = User
    template_name = "registration/signup.html"


class JobSeekerSignUpView(CreateView):
    model = User
    form_class = JobSeekerSignUpForm
    template_name = 'registration/jobseekersignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'jobseeker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('jobseeker_home')
 
 
class BusinessSignUpView(CreateView):
    model = User
    form_class = BusinessSignUpForm
    template_name = 'registration/businesssignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'business'
        return super().get_context_data(**kwargs)
        
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('business_home')  
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_jobseeker:
            Jobseeker.objects.create(user=instance)
        elif instance.is_business:
            Business.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_jobseeker:
        instance.jobseeker.save()
    elif instance.is_business:
        instance.business.save()
