from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from accounts.forms import NewJobSeekerForm, NewBusinessForm

# Create your views here.
def signupjobseeker(request):
    if request.method == "POST":
        form = NewJobSeekerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)

def signupbusiness(request):
    if request.method == "POST":
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)