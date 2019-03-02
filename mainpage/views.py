import mimetypes
import os
from time import sleep
from threading import Thread
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from MangaSite import settings


def timed():
    sleep(30)


class Index(View):
    @staticmethod
    def get(request):
        t = Thread(target=timed)
        t.start()
        return render(request, 'mainpage/index.html')


class Mainpage(View):
    @staticmethod
    def get(request):
        return render(request, 'mainpage/mainpage.html')


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
