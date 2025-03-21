from django.shortcuts import render
from django.http import HttpRequest

def render_contacts(request: HttpRequest):
    return render(
        request = request,
        template_name = "contacts.html",
        context = {
            'authenticated': request.user.is_authenticated
        }
        )

# Create your views here.
