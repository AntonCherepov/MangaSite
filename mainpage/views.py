import mimetypes
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from MangaSite import settings
from mainpage.models import News, User


class Mainpage(View):
    @staticmethod
    def get(request):
        news = News.objects.all()
        return render(request, 'mainpage/mainpage.html', {"news": news})


class Index(View):
    @staticmethod
    def get(request):
        news = News.objects.get(id=1)
        news_files = news.zip_file.all()
        context = {"news": [{"url": os.path.join("media",
                            str(i.file_path)),
                            "file_name": str(i.file_path)}
                            for i in news_files]}
        return render(
            request,
            'mainpage/index.html', context
            )

'''
class DownloadFile(View):
    @staticmethod
    def get(request, download_name):
        file = '/' + 'test.jpg'
        fp = open(settings.MEDIA_DIR + file, "rb")
        response = HttpResponse(fp.read())
        fp.close()
        file_type = mimetypes.guess_type(settings.MEDIA_DIR + file)
        if file_type is None:
            file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(
            os.stat(settings.MEDIA_DIR + file).st_size)
        response['Content-Disposition'] = "attachment; filename='test.jpg'"
        return response
'''