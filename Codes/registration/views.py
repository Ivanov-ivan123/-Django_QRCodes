from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest
# from .models import MyUser

def render_registretion(request: HttpRequest):
    password_error = False
    create_user_error = False
    print("registration start", "\n", "request.method =", request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            try:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=name,
                    last_name=surname
                )
                return redirect('authorization')
            except:
                create_user_error = True
        else:
            password_error = True
        
    return render(
        request=request,
        template_name='registration.html',
        context = {
            'authenticated': request.user.is_authenticated,
            'password_error': password_error,
            'create_user_error': create_user_error
        }
    )
