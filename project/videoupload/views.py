from django.shortcuts import render, redirect
from .models import VideoData
from django.contrib.auth.decorators import login_required

# @login_required
def VideoUpload(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')

        # Get uploaded file
        video_file = request.FILES.get('video_file')
        thumbnail = request.FILES.get('thumbnail')

        # Save into database
        VideoData.objects.create(
        title=title,
        description=description,
        video_file=video_file,
        thumbnail=thumbnail,
        uploaded_by=request.user
        )

        return redirect('home')

    return render(request, "upload.html")