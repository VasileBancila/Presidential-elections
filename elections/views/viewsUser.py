from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import CreateUserForm, EditProfileDescriptionForm
from ..models import ElectionRanking, ElectionRound

def register_user(request):
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
        return render(request, 'elections/register.html', context)

def login_user(request):
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
                messages.error(request, 'Username or Password is incorrect')
                
        return render(request, 'elections/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileDescriptionForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return redirect('user_profile')
    else:
        profile_form = EditProfileDescriptionForm()

    user = request.user
    
    try:
        current_round = ElectionRound.objects.get(ongoing=True)
        existing_candidate = ElectionRanking.objects.filter(candidate=user, election_round=current_round).exists()    
    except ElectionRound.DoesNotExist:
        current_round = None
        existing_candidate = False
    
    context = {'profile_form': profile_form, 'existing_candidate': existing_candidate, 'current_round': current_round}

    return render(request, 'elections/user_profile.html', context)