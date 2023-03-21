from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import JobSeekerSignUpView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('jobseekersignup/', JobSeekerSignUpView.as_view(), name="jobseekersignup")
]