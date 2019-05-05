from django.conf.urls.static import static
from django.urls import path
from MangaSite import settings
from .views import Registration, Login

urlpatterns = [
    path('registration', Registration.as_view(), name='registration'),
    path('auth', Login.as_view(), name='auth')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
