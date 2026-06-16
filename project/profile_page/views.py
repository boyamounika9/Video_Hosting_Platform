from django.shortcuts import render
from videoupload.models import VideoData
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

    current_user = request.user

    videos = VideoData.objects.filter(uploaded_by=current_user)

#for video count in profile page
    video_count = videos.count()

    return render(request, 'profile.html', {
        'user_data': current_user,
        'Videos': videos,
        'video_count': video_count
    })
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def delete_video(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(VideoData, id=video_id)
        if video.uploaded_by == request.user:
            # Delete the video files from storage
            if video.video_file:
                video.video_file.delete(save=False)
            if video.thumbnail:
                video.thumbnail.delete(save=False)
            video.delete()
            messages.success(request, "Video deleted successfully.")
        else:
            return HttpResponseForbidden("You are not allowed to delete this video.")
    return redirect('profile')
