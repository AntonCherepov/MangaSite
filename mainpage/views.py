from os import path
from django.shortcuts import render
from django.views.generic import View
from mainpage.models import News


class Mainpage(View):
    @staticmethod
    def get(request):
        news = News.objects.order_by("-id")
        context = {"news": news}
        return render(request, 'mainpage/mainpage.html', context)


class Index(View):
    @staticmethod
    def get(request):
        news = News.objects.get(id=1)
        news_files = news.zip_file.all()
        context = {"news_files": [{"url": path.join("media",
                                                       str(i.file_path)),
                                   "file_name": str(i.file_name)}
                                  for i in news_files]}
        return render(
            request,
            'mainpage/index.html', context
        )
