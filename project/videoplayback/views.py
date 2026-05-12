from django.shortcuts import render, get_object_or_404
from videoupload.models import VideoData


def playback(request, video_id):

    video = get_object_or_404(VideoData, id=video_id)

    suggested_videos = VideoData.objects.exclude(id=video_id)

    context = {
        'video': video,
        'suggested_videos': suggested_videos
    }

    return render(request, 'playback.html', context)