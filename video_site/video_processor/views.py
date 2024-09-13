from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from .tasks import extract_subtitles
import ffmpeg
from celery import shared_task
from .models import Video

from django.db.models import Q
import re

def search_subtitles(request, video_id):
    query = request.GET.get('q')
    video = Video.objects.get(pk=video_id)
    
    with open(video.subtitle_file.path, 'r') as f:
        subtitles = f.readlines()

    result = []
    for i, line in enumerate(subtitles):
        if re.search(query, line, re.IGNORECASE):
            timestamp = subtitles[i-1]
            result.append((timestamp, line))

    return render(request, 'search_results.html', {'results': result, 'video': video})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            print("DATA SUBMITTED")
            
            extract_subtitles.delay(video.id)  # Background processing
            print("DATA EXTRACTION")
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'video_detail.html', {'video': video})

# Create your views here.
