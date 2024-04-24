from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Profile, Voter, ElectionRanking, ElectionRound

@login_required(login_url='login')
def home(request):
    try:
        round = ElectionRound.objects.get(ongoing=True)
        candidates = ElectionRanking.objects.filter(election_round=round).order_by('-no_votes')
        context = {'candidates': candidates, 'round': round}
    except ElectionRound.DoesNotExist:
        messages.error(request, 'There are no elections in progress!')
        context = {}
    except ElectionRanking.DoesNotExist:
        messages.error(request, 'No candidate registered for the election!')
        context = {}

    return render(request, 'elections/home.html', context)

def registerCandidacy(request):
    user = request.user
    current_election_round = ElectionRound.objects.get(ongoing=True)
    existing_candidate = ElectionRanking.objects.filter(candidate=user, election_round=current_election_round).exists()

    if request.method == 'POST' and not existing_candidate:
        new_ranking = ElectionRanking(candidate=user, election_round=current_election_round)
        new_ranking.save()
        messages.success(request, "You have been successfully registered for this election round.")
    else:
        messages.error(request, "You are already registered for this election round.")

    return redirect('userProfile')

def candidateProfile(request, id):
    candidate_profile = Profile.objects.get(user=id)
    if candidate_profile:
        profile = candidate_profile
    else:
        profile = None

    context = {'profile': profile}
    return render(request, 'elections/candidateProfile.html', context)

# def voteCandidate(request, user_id):
#     if request.method == 'POST':
#         user = request.user
#         voter = Profile.objects.get(user_id=user)
#         candidate = Profile.objects.get(user_id=user_id)
        
#         if voter.user != candidate.user:
#             if not voter.voted:
#                 candidate.no_votes += 1
#                 candidate.save()
#                 voter.voted = True
#                 voter.save()
#                 messages.success(request, 'Your vote has been registered for ' + str(candidate.user) + "!")
#             else:
#                 messages.error(request, 'You have already voted!')
#         else:
#             messages.error(request, "You can't vote for yourself!")
    
#     return redirect('home')

# def electionRounds(request):
#     return render(request, 'elections/electionRounds.html')