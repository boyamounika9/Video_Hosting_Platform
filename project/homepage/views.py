from django.shortcuts import render
from videoupload.models import VideoData

# Create your views here.

def home(request):
    videos = VideoData.objects.all()
    return render(request, 'home.html', {'videos': videos})