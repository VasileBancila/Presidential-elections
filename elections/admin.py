from django.contrib import admin
from .models import Profile, Candidate, CandidacyAndVot

# Register your models here.

admin.site.register(Profile)
admin.site.register(CandidacyAndVot)
admin.site.register(Candidate)