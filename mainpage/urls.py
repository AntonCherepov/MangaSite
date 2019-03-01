from django.urls import path
from .views import Index, Mainpage

urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path('index', Index.as_view(), name='index')

]
