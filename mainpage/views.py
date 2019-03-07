import os
from django.shortcuts import render
from django.views.generic import View
from mainpage.models import News


class Mainpage(View):
    @staticmethod
    def get(request):
        news = News.objects.order_by("-id")
        return render(request, 'mainpage/mainpage.html', {"news": news})


class Index(View):
    @staticmethod
    def get(request):
        news = News.objects.get(id=1)
        news_files = news.zip_file.all()
        context = {"news_files": [{"url": os.path.join("media",
                                                       str(i.file_path)),
                                   "file_name": str(i.file_path)}
                                  for i in news_files]}
        return render(
            request,
            'mainpage/index.html', context
        )
