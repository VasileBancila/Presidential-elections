from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('registration/', views.registrationUser, name='registration'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('registerCandidacy/', views.registerCandidacy, name='registerCandidacy'),
    path('candidateProfile/<user_id>', views.candidateProfile, name='candidateProfile'),
    path('voteCandidate/<user_id>', views.voteCandidate, name='voteCandidate'),
    
]