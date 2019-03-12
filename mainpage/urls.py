from django.conf.urls.static import static
from django.urls import path

from MangaSite import settings
from .views import Index, Mainpage #, DownloadFile

urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('index', Index.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
