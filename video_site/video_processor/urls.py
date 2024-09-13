from django.urls import path
from .views import upload_video, video_list, video_detail, search_subtitles

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:pk>/', video_detail, name='video_detail'),
    path('videos/<int:video_id>/search/', search_subtitles, name='search_subtitles'),
]
