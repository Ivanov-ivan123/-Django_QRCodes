from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

def render_authorization(request: HttpRequest):
    fail = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request = request,
            username = username,
            password = password
        )
        print("is_authenticated =", request.user.is_authenticated)
        if user:
            login(request = request, user = user)
            return redirect("main")
        else:
            fail = True
    return render(
        request=request,
        template_name='authorization.html',
        context = {
            'fail': fail,
            'authenticated': request.user.is_authenticated
            }
    )
    
def render_logout(request):
    logout(request = request)
    return redirect('authorization')