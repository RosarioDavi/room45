from django.contrib import admin
from accounts.models import User, Jobseeker, Business

admin.site.register(User),
admin.site.register(Jobseeker),
admin.site.register(Business)