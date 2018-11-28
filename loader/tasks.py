from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Link





@shared_task
def email():

    send_mail('Hello from Iskender.',Link.objects.all().last().link, 'iberdiev@zoho.com', [Link.objects.all().last().email
], fail_silently=False)


# from os import system
# import cgi
# form = cgi.FieldStorage()
# link = form.getvalue('Link')
# system(link)

from os import system, listdir, remove


def delete():

    listOfFiles = listdir('media/.')
    for i in listOfFiles:
        if i.startswith("download"):
            name = i
            remove('media/{}'.format(name))

def download():
    link = Link.objects.all().last().link
    system("youtube-dl -o 'media/download' {}".format(link))

def convert():
    listOfFiles = listdir('media/.')
    for i in listOfFiles:
        if i.startswith("download"):
            name = i
            system("ffmpeg -i 'media/{}' 'media/download.mp3'".format(name))
@shared_task
def download_convert():



    delete()
    download()
    convert()
