from django.urls import path
from .views import render_create_code, render_redirect

urlpatterns = [
    path("", render_create_code, name = "create_code"),
    # path("qr-redirection/", render_redirect, name = "redirection"),
    path("<int:pk>", render_redirect, name = "redirection")
]