from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
]