from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.VideoUpload, name='upload'),
    path('edit/<int:video_id>/', views.EditVideo, name='edit_video'),
]