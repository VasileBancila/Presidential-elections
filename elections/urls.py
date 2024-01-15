from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('registration/', views.registrationUser, name='registration'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
]