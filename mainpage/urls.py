from django.urls import path
from .views import Index, Mainpage, DownloadFile

urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('index', Index.as_view(), name='index'),
    path('download_file', DownloadFile.as_view(), name='download_file')

]
