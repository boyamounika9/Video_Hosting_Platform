from django.urls import path
from . import views

urlpatterns = [
    path('playback/<int:video_id>/', views.playback, name='playback'),
]