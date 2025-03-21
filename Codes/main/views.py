from django.shortcuts import render, redirect
from Codes import settings
from .forms import SubForm
from .models import Subscription
from django.http import HttpRequest

def render_main(request: HttpRequest):
    if request.method == "POST":
        if request.user:
            sub = SubForm(request.POST)

            if sub.is_valid():
                    sub.save(user_id = request.user.id)
                    return redirect("create_code")
        else:
            return redirect("registration")
    else:
        sub = SubForm()
    return render(
        request = request,
        template_name = "main.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "form": sub,
        }
    )
# Create your views here.
