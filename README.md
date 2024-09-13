# VideoSubtitleExtraction
Steps to follow:-
(I have done implementation on Ubuntu OS)
1.Install Redis:-
sudo apt install redis-server
2.Start Redis:-
redis-server/sudo systemctl start redis(if set up as a service)
3.check if it is running:-
redis-cli ping
4.if response is PONG,then it is running
Now start the celery
celery -A video_site beat --loglevel=info
Then start django server:-
python manage.py runserver

