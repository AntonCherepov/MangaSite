from django.conf.urls.static import static
from django.urls import path
from MangaSite import settings
from .views import (Index, Mainpage, Projects,
                    Team, ProjectInfo, Registration,
                    Login, NewsInfo)

urlpatterns = [
    path('', Mainpage.as_view(), name="mainpage"),
    path('<int:page>', Mainpage.as_view(), name='mainpage'),
    path('index', Index.as_view(), name='index'),
    path('projects', Projects.as_view(), name='projects'),
    path('team', Team.as_view(), name='team'),
    path('registration', Registration.as_view(), name='registration'),
    path('auth', Login.as_view(), name='auth'),
    path('projects/<str:project_name>/', ProjectInfo.as_view(),
         name='project_info'),
    path('news/<int:news_id>/', NewsInfo.as_view(), name='news_info')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
