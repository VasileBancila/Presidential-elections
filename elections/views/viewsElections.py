from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Profile, CandidacyAndVot, Candidate

@login_required(login_url='login')
def home(request):
    try:
        candidates = Candidate.objects.all()
        candidates = candidates.order_by('-no_votes')
    except Candidate.DoesNotExist:
        candidates = None

    context = {'candidates': candidates}
    return render(request, 'elections/home.html', context)

def registerCandidacy(request):
    user = request.user
    candidacy = CandidacyAndVot.objects.get(user=user)
    
    if request.method == 'POST' and not candidacy.election_candidacy:
        candidate = Candidate.objects.create(user=user)
        candidate.save()
        candidacy.election_candidacy = True
        candidacy.save()

    return redirect('userProfile')

def candidateProfile(request, user_id):
    candidate_profile = Profile.objects.get(user_id=user_id)
    if candidate_profile:
        profile = candidate_profile
    else:
        profile = None

    context = {'profile': profile}
    return render(request, 'elections/candidateProfile.html', context)

def voteCandidate(request, user_id):
    if request.method == 'POST':
        user = request.user
        voter = CandidacyAndVot.objects.get(user_id=user)
        candidate = Candidate.objects.get(user_id=user_id)
        
        if voter.user != candidate.user:
            if not voter.voted:
                candidate.no_votes += 1
                candidate.save()
                voter.voted = True
                voter.save()
                messages.success(request, 'Your vote has been registered for ' + str(candidate.user) + "!")
            else:
                messages.error(request, 'You have already voted!')
        else:
            messages.error(request, "You can't vote for yourself!")
    
    return redirect('home')