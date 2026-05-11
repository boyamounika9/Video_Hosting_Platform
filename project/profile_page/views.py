from django.shortcuts import render
from videoupload.models import VideoData
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

    current_user = request.user
    videos = VideoData.objects.filter(uploaded_by=current_user)

    return render(request, 'profile.html', {
        'user_data': current_user,
        'Videos': videos
    })