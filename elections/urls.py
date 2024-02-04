from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registrationUser, name='registration'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('home/', views.home, name='home'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('candidateProfile/<user_id>/', views.candidateProfile, name='candidateProfile'),
    path('registerCandidacy/', views.registerCandidacy, name='registerCandidacy'),
    path('voteCandidate/<user_id>/', views.voteCandidate, name='voteCandidate'),
]