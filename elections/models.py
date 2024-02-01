from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    
    def __str__(self): 
        return self.user.username

class CandidacyAndVot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    election_candidacy = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)
    
    def __str__(self): 
        return self.user.username

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_votes = models.IntegerField(default=0)
        
    def __str__(self): 
        return self.user.username