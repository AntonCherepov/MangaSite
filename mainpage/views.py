from os import path
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from mainpage.models import News, Project


class Mainpage(View):
    @staticmethod
    def get(request):
        news = News.objects.order_by("-id")[:5]
        context = {"news": news}
        return render(request, "mainpage/mainpage.html", context)


class Team(View):
    @staticmethod
    def get(request):
        return render(request, "mainpage/team.html")


class Projects(View):
    @staticmethod
    def get(request):
        active_projects = Project.objects.filter(status="active")
        dropped_projects = Project.objects.filter(status="dropped")
        maybe_projects = Project.objects.filter(status="maybe")
        finished_projects = Project.objects.filter(status="finished")
        all_projects = [active_projects, dropped_projects, 
                        maybe_projects, finished_projects]
        context = {"all_projects": all_projects}
        return render(request, "mainpage/projects.html", context)


class ProjectInfo(View):
    @staticmethod
    def get(request, project_name):
        project = get_object_or_404(Project, name=project_name)
        context = {"project": project}
        return render(request, "mainpage/project_info.html", context)


class Index(View):
    @staticmethod
    def get(request):
        news = News.objects.get(id=1)
        news_files = news.zip_file.all()
        context = {"news_files": [{"url": path.join("media", str(i.file_path)),
                                   "file_name": str(i.name)}
                                  for i in news_files]}
        return render(request, "mainpage/index.html", context)
