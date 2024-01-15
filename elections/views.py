from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import CreateUserForm

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
     return render(request, 'elections/profile.html')