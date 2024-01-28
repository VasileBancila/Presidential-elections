from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import CreateUserForm, EditProfileDescriptionForm

@login_required(login_url='login')
def home(request):
    try:
        candidates = Candidate_Status.objects.all()
        candidates = candidates.order_by('-no_votes')
    except Candidate_Status.DoesNotExist:
        candidates = None

    context = {'candidates': candidates}
    return render(request, 'elections/home.html', context)

def registrationUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Acount was created for ' + user)
                return redirect('login')
                
        context = {'form': form}
        return render(request, 'elections/registration.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
                
        return render(request, 'elections/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        profile_form = EditProfileDescriptionForm(request.POST, request.FILES, instance=request.user.profiles)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return redirect('users-profile')
    else:
        profile_form = EditProfileDescriptionForm()

    return render(request, 'elections/profile.html', {'profile_form': profile_form})

def register_candidate(request):
    if request.method == 'POST':
        user = request.user
        candidate_status = Candidate_Status.objects.create(user=user)
        candidate_status.save()
        candidate_status.election_candidacy = True
        candidate_status.save()
        return redirect('users-profile')
    else:
        return render(request, 'elections/profile.html')

def candidate_profile(request, user_id):
    candidate_profile = Profiles.objects.get(user_id=user_id)
    if candidate_profile:
        profile = candidate_profile
    else:
        profile = None

    context = {'profile': profile}
    return render(request, 'elections/candidate_profile.html', context)