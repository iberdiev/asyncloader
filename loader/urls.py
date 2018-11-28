from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('history/', views.HistoryPageView.as_view(), name='history'),
    path('download/', views.DownloadPageView.as_view(), name='download'),
    path('download/confirm', views.Confirm.as_view(), name='confirm'),
    path('email/', views.email_page, name='email')
]
