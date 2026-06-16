from django.shortcuts import render, redirect
from .models import VideoData
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import traceback

@login_required
def VideoUpload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get('video_file')
        thumbnail = request.FILES.get('thumbnail')

        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        if not video_file or not thumbnail:
            msg = "Both video and thumbnail files are required."
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': msg}, status=400)
            messages.error(request, msg)
            return render(request, "upload.html")

        try:
            VideoData.objects.create(
                title=title,
                description=description,
                video_file=video_file,
                thumbnail=thumbnail,
                uploaded_by=request.user
            )
            msg = "Video uploaded successfully!"
            if is_ajax:
                messages.success(request, msg)
                return JsonResponse({'status': 'success', 'redirect_url': '/'})
            messages.success(request, msg)
            return redirect('home')
        except Exception as e:
            msg = f"An error occurred during upload: {str(e)}"
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': msg}, status=500)
            messages.error(request, msg)
            return render(request, "upload.html")

    return render(request, "upload.html")

from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required
def EditVideo(request, video_id):
    video = get_object_or_404(VideoData, id=video_id)
    if video.uploaded_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this video.")

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get('video_file')
        thumbnail = request.FILES.get('thumbnail')

        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        try:
            video.title = title
            video.description = description
            if video_file:
                video.video_file = video_file
            if thumbnail:
                video.thumbnail = thumbnail
            video.save()
            
            msg = "Video updated successfully!"
            if is_ajax:
                messages.success(request, msg)
                return JsonResponse({'status': 'success', 'redirect_url': '/profile/'})
            messages.success(request, msg)
            return redirect('profile')
        except Exception as e:
            msg = f"An error occurred during update: {str(e)}"
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': msg}, status=500)
            messages.error(request, msg)
            return render(request, "upload.html", {'video': video})

    return render(request, "upload.html", {'video': video})
