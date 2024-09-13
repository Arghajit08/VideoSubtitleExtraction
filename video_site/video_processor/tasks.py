import ffmpeg
from celery import shared_task
from .models import Video

@shared_task
def extract_subtitles(video_id):
    print("DATA RECEIVED")
    video = Video.objects.get(id=video_id)
    subtitle_path = f'subtitles/{video.title}.srt'
    
    # Extract subtitles with ffmpeg
    ffmpeg.input(video.video_file.path).output(subtitle_path, format='srt').run()
    
    video.subtitle_file = subtitle_path
    video.save()
