from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User as Auth_user
from django.db import IntegrityError
from users.models import Profile


class Registration(View):
    @staticmethod
    def get(request):
        return render(request, "users/registration.html")

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
            return render(request, "users/registration.html", context)
        except IntegrityError:
            context = {"err": "Произошла ошибка! Возможно пользователь с "
                              "таким именем уже зарегистрирован."}
            return render(request, "users/registration.html", context)
        return render(request, "users/registration_finished.html")


class Login(View):
    @staticmethod
    def get(request):
        return render(request, "users/auth.html")

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
        return render(request, "users/auth.html")
