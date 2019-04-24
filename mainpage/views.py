from os import path
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User as Auth_user
from mainpage.models import News, Project, Profile, Comment


class Mainpage(View):
    @staticmethod
    def get(request, page=1):
        news = News.objects.order_by("-id")
        paginator = Paginator(news, 4)
        # page = request.GET.get("page")
        page_obj = paginator.get_page(page)
        context = {"page_obj": page_obj, "paginator": paginator}
        return render(request, "mainpage/mainpage.html", context)


class Team(View):
    @staticmethod
    def get(request):
        users = Profile.objects.filter(to_show=True)
        context = {"users": users}
        return render(request, "mainpage/team.html", context)


class Projects(View):
    @staticmethod
    def get(request):
        active_projects = Project.objects.filter(status="active")
        dropped_projects = Project.objects.filter(status="dropped")
        maybe_projects = Project.objects.filter(status="maybe")
        finished_projects = Project.objects.filter(status="finished")
        all_projects = [active_projects, dropped_projects,
                        maybe_projects, finished_projects]
        for i in [*all_projects]:
            if not i:
                all_projects.pop(all_projects.index(i))
        context = {"all_projects": all_projects}
        if not all_projects:
            context = {"all_projects": "no content"}
        return render(request, "mainpage/projects.html", context)


class ProjectInfo(View):
    @staticmethod
    def get(request, project_name):
        project = get_object_or_404(Project, name=project_name)
        context = {"project": project}
        return render(request, "mainpage/project_info.html", context)


class NewsInfo(View):
    @staticmethod
    def get(request, news_id):
        news = get_object_or_404(News, id=news_id)
        comments = Comment.objects.filter(news_id=news_id)
        context = {"news": news, "comments": comments}
        return render(request, "mainpage/news_info.html", context)

    @staticmethod
    def post(request, news_id):
        news = get_object_or_404(News, id=news_id)
        user = request.user
        text = request.POST.get('comment')
        u = user.comment_set.create(text=text)
        u.news_id = news_id
        u.save()
        comments = Comment.objects.filter(news_id=news_id)
        context = {"news": news, "comments": comments}
        return render(request, "mainpage/news_info.html", context)


class Registration(View):
    @staticmethod
    def get(request):
        return render(request, "mainpage/registration.html")

    @staticmethod
    def post(request):
        username = request.POST.get("login")
        password = request.POST.get("password")
        email = request.POST.get("email")
        try:
            user = Auth_user.objects.create_user(username=username,
                                                 email=email,
                                                 password=password)
            profile = Profile(user=user, name=username)
            user.save()
            profile.save()
        except ValueError:
            context = {"err": "Для регистрации необходимо ввести логин!"}
            return render(request, "mainpage/registration.html", context)
        except IntegrityError:
            context = {"err": "Произошла ошибка! Возможно пользователь с "
                              "таким именем уже зарегистрирован."}
            return render(request, "mainpage/registration.html", context)
        return render(request, "mainpage/registration_finished.html")


class Login(View):
    @staticmethod
    def get(request):
        return render(request, "mainpage/auth.html")

    @staticmethod
    def post(request):
        print(request)
        if str(request.POST.get("logout")) == "logout":
            logout(request)
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
        return render(request, "mainpage/auth.html")


class Index(View):
    @staticmethod
    def get(request):
        news = News.objects.get(id=1)
        news_files = news.zip_file.all()
        context = {"news_files": [{"url": path.join("media", str(i.file_path)),
                                   "file_name": str(i.name)}
                                  for i in news_files]}
        return render(request, "mainpage/index.html", context)


'''
    model = News
    paginate_by = 2
    template_name = "mainpage/mainpage.html"
    queryset = News.objects.order_by("-id")
'''
