from django.shortcuts import render
from create_code.models import Code
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
import os
from Codes.settings import BASE_DIR
from django.http import FileResponse

# Create your views here.

@login_required
def render_my_codes_page(request: HttpRequest):
    codes = Code.objects.filter(creator = request.user)

    if request.method == "POST":
        code_name = request.POST.get("image_name")
        response = FileResponse(open(os.path.join(str(BASE_DIR) + "/media/" + str(request.user)) + f"/{code_name}.png", "rb"), as_attachment = True)
        return response

    return render(
        request = request,
        template_name = "my_codes.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "user": request.user,
            "codes": codes
        }
    )