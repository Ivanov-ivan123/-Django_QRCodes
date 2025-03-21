from .views import render_authorization, render_logout
from django.urls import path, include

urlpatterns = [
    path('', render_authorization, name = 'authorization'),
    path('logout/', render_logout, name = 'logout')
]