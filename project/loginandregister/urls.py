from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('playback/', views.playback, name='playback'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
]