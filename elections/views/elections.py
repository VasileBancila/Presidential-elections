from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Profile, Voter, ElectionRanking, ElectionRound
from django.contrib.auth.models import User
from django.utils import timezone

def check_round_expiration():
    rounds = ElectionRound.objects.all()
    current_time = timezone.now().date()

    for round in rounds:
        if round.end_date < current_time:
            round.ongoing = False
            round.save()

@login_required(login_url='login')
def home(request):
    check_round_expiration()
    try:
        round = ElectionRound.objects.get(ongoing=True)
        candidates = ElectionRanking.objects.filter(
            election_round=round).order_by('-no_votes')
        context = {'candidates': candidates, 'round': round}
    except ElectionRound.DoesNotExist:
        messages.error(request, 'There are no elections in progress!')
        context = {}
    except ElectionRanking.DoesNotExist:
        messages.error(request, 'No candidate registered for the election!')
        context = {}

    return render(request, 'elections/home.html', context)

def register_candidacy(request):
    user = request.user
    current_election_round = ElectionRound.objects.get(ongoing=True)
    existing_candidate = ElectionRanking.objects.filter(
        candidate=user, election_round=current_election_round).exists()

    if request.method == 'POST' and not existing_candidate:
        new_ranking = ElectionRanking(
            candidate=user, election_round=current_election_round)
        new_ranking.save()
        messages.success(request, \
            "You have been successfully registered for this election round.")
    else:
        messages.error(
            request, "You are already registered for this election round.")

    return redirect('user_profile')

def candidate_profile(request, id):
    candidate_profile = Profile.objects.get(user=id)
    if candidate_profile:
        profile = candidate_profile
    else:
        profile = None

    context = {'profile': profile}
    return render(request, 'elections/candidate_profile.html', context)

def vote_candidate(request, candidate_id):
    if request.method == 'POST':
        voter = request.user
        candidate_user = User.objects.get(id=candidate_id)
        current_election_round = ElectionRound.objects.get(ongoing=True)
        current_candidate = ElectionRanking.objects.get(
            candidate=candidate_user, election_round=current_election_round)
        existing_vote = Voter.objects.filter(
            user_votes=voter, election_round=current_election_round).exists()
        
        if voter != current_candidate.candidate:
            if not existing_vote:
                current_candidate.no_votes += 1
                current_candidate.save()
                
                new_voter = Voter(
                    user_votes=voter, 
                    election_round=current_election_round, 
                    candidate=current_candidate)
                new_voter.save()
                messages.success(request, 'Your vote has been registered for '
                                 + str(current_candidate.candidate) + "!")
            else:
                messages.error(request, 'You have already voted!')
        else:
            messages.error(request, "You can't vote for yourself!")
    
    return redirect('home')

def election_rounds(request):
    rounds = ElectionRound.objects.all()
    return render(
        request, 'elections/election_rounds.html', {'rounds': rounds})

def round_ranking(request, round_id):
    round = ElectionRound.objects.get(id=round_id)
    ranking = ElectionRanking.objects.filter(
        election_round=round).order_by('-no_votes')
    context = {'ranking': ranking, 'round': round}
    return render(request, 'elections/round_ranking.html', context)