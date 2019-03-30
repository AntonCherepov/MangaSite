from django.conf.urls.static import static
from django.urls import path
from MangaSite import settings
from .views import Index, Mainpage, Projects, Team, ProjectInfo

urlpatterns = [
    path('', Mainpage.as_view(), name="mainpage"),
    path('<int:page>', Mainpage.as_view(), name='mainpage'),
    path('index', Index.as_view(), name='index'),
    path('projects', Projects.as_view(), name='projects'),
    path('team', Team.as_view(), name='team'),
    path('projects/<str:project_name>/',
         ProjectInfo.as_view(),
         name='project_info'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
