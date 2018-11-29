from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Link
from django.views.generic.edit import CreateView
# from django.core.mail import send_mail
from .tasks import email
# from celery.result import AsyncResult


class HomePageView(TemplateView):
    template_name = "loader/index.html"


class HistoryPageView(ListView):
    model = Link
    template_name = "loader/history.html"


class DownloadPageView(CreateView):
    model = Link
    template_name = 'loader/download.html'
    fields = '__all__'


class Confirm(ListView):
    model = Link
    template_name = "loader/confirm.html"

def email_page(request):
    email.delay()
    return render(request, 'loader/email.html')
