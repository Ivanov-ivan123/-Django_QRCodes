"""
URL configuration for Codes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registration.views import render_registretion
from main.views import render_main
from contacts.views import render_contacts
from my_codes.views import render_my_codes_page
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_main, name='main'),
    path('auth/', include("authorization.urls")),
    path('reg/', render_registretion, name='registration'),
    path('contacts/', render_contacts, name='contacts'),
    path('my_codes/', render_my_codes_page, name = "my_codes"),
    path('create_code/', include("create_code.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
