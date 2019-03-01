from django.shortcuts import render
from django.template import loader
#print(loader.get_template('/mainpage.html'))


def mainpage(request):
    #MangaSite / templates / mainpage / mainpage.html
    return render(request, 'mainpage/mainpage.html')


def index(request):
    return render(request, 'index.html')
