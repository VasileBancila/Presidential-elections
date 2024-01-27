from django.db import models
from django.contrib.auth.models import User

class Candidate_Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    election_candidacy = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)
    no_votes = models.IntegerField(default=0)
        
    def __str__(self):
        #status = self.user.username + "--> vote :" + str(self.voted) + "--> candidacy :" + str(self.election_candidacy) + "--> no_votes: " + str(self.no_votes) 
        return self.user.username

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    
    def __str__(self):
        #profile = self.user.username + "--> is_public :" + str(self.is_public) + "--> description :" + self.description 
        return self.user.username