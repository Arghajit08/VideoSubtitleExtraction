from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.FileField(upload_to='subtitles/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
