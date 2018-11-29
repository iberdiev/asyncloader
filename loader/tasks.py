from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Link


from os import system, listdir, remove








@shared_task
def email():

    listOfFiles = listdir('media/.')
    for i in listOfFiles:
        if i.startswith("download"):
            name = i
            remove('media/{}'.format(name))

    link = Link.objects.all().last().link
    system("youtube-dl -o 'media/download' {}".format(link))

    listOfFiles = listdir('media/.')
    for i in listOfFiles:
        if i.startswith("download"):
            name = i
            system("ffmpeg -i 'media/{}' 'media/download.mp3'".format(name))



    send_mail('Hello from Iskender.',"http://127.0.0.1:8000/media/download.mp3", 'iberdiev@zoho.com', [Link.objects.all().last().email
], fail_silently=False)
