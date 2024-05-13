from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user-profile/', views.user_profile, name='user_profile'),
    
    path('home/', views.home, name='home'),
    path('candidate-profile/<id>/', views.candidate_profile, name='candidate_profile'),
    path('register-candidacy/', views.register_candidacy, name='register_candidacy'),
    path('vote-candidate/<candidate_id>/', views.vote_candidate, name='vote_candidate'),
    path('election-rounds/', views.election_rounds, name='election_rounds'),
    path('round-ranking/<round_id>/', views.round_ranking, name='round_ranking'),
]