from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self): 
        return self.user.username
    
class ElectionRound(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    ongoing = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Voter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election_rounds = models.ManyToManyField(ElectionRound)
    has_voted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ("user", "election_round")

class ElectionRanking(models.Model):
    election_round = models.ForeignKey(ElectionRound, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    no_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.election_round} - {self.candidate.username}"

    class Meta:
        unique_together = ("election_round", "candidate")