"""config URL Configuration
장고의 Default Url Conf 파일 입니다.
다른 앱들의 경로를 include 받아 분기 처리 시켜줍니다.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    # ALLAUTH
    path('accounts/', include('allauth.urls')),
    # User
    path('users/', include('apps.user.urls')),
    # your different app include here ⬇  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
