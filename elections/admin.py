from django.contrib import admin
from .models import Profile, ElectionRanking, ElectionRound, Voter

# Register your models here.

admin.site.register(Profile)
admin.site.register(ElectionRanking)
admin.site.register(ElectionRound)
admin.site.register(Voter)