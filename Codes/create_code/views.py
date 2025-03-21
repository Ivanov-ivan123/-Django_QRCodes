from django.shortcuts import render, redirect
import qrcode, os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Code
from main.models import Subscription
import datetime
from PIL import Image


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Create your views here.
@login_required
def render_create_code(request: HttpRequest):
    # creation_error = False
    number_error = False
    code = False
    user_status = False
    desktop_quantity = False
    desktop = False
    user = request.user
    is_desktop_mess_error = False
    is_not_desktop_mess_error = False
    subscription = Subscription.objects.filter(user_id = user.id)
    for pk in range(len(subscription)):
        user_status = subscription[pk].subscription
        desktop_quantity = subscription[pk].desktopQuantity
        print("user_status =", user_status)
    if user_status == "Pro":
        max_qr_num = 100
    elif user_status == "Standart":
        max_qr_num = 10
    elif not user_status:
        max_qr_num = 1
    else:
        max_qr_num = int(desktop_quantity) * 5
        print("Is desktop subscription -", max_qr_num)
        desktop = True

    print("max_qr_number", max_qr_num)
    num_qr = Code.objects.filter(creator_id = user.id)
    num_qr = (len(num_qr))
    print("num_qr =", num_qr)
    prymary_key = Code.objects.last().id + 1
    print("primare_key =", prymary_key)

    if num_qr < max_qr_num:
        if request.method == 'POST':
            title = request.POST.get('title')
            url = request.POST.get('url')
            description = request.POST.get('description')
            color = request.POST.get("color")
            bg_color = request.POST.get("bg_color")
            embaded_img = request.FILES.get("center_image")
            version = request.POST.get("version")
            radius = request.POST.get("radius")

            print("desctop =", desktop)
            if desktop:
                try:
                    print("deskt", url.split("//")[1])
                    is_not_desktop_mess_error = True
                except:
                    pass
            
            elif not desktop:
                try:
                    print("not deskt", url.split("//")[1])
                except:
                    is_desktop_mess_error = True

            print("desktop message errors:", int(is_desktop_mess_error), int(is_not_desktop_mess_error))
            if not is_desktop_mess_error and not is_not_desktop_mess_error:
                print("user_subscription =", user_status)
                folder_path = f"media/{request.user}"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                qrcode_image_path = f'{folder_path}/{title}.png'
                qr = qrcode.QRCode(
                    version = version,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 15,
                    border = 2
                )
                if user_status == "Pro" or user_status == "Standart" or desktop:
                    print("amazing user qrcode creation")
                    print(title, "\n", url, "\n", description, "\n", color, "\n", bg_color, "\n", embaded_img, "\n", radius)

                    # try:
                    
                    if not desktop:
                        qr.add_data(f"http://127.0.0.1:8000/create_code/{prymary_key}")
                        # qr.add_data("http://127.0.0.1:8000/create_code/qr-redirection")
                    elif desktop:
                        print("add desktop data")
                        qr.add_data(url)
                    qr.make(fit = True)
                    image = qr.make_image(
                        image_factory = StyledPilImage,
                        eye_drawer = RoundedModuleDrawer(radius_ratio = float(radius)),
                        module_drawer = RoundedModuleDrawer(radius_ratio = float(radius)),
                        color_mask = SolidFillColorMask(back_color = hex_to_rgb(bg_color), front_color = hex_to_rgb(color)),
                    )
                    if embaded_img:
                        center_iamge = Image.open(embaded_img).resize((75, 75), Image.LANCZOS)
                        offset = ((image.size[0] - 75) // 2, (image.size[1] - 75) // 2)
                        image.paste(center_iamge, offset, mask = center_iamge.split()[3] if center_iamge == "RGBA" else None)
                    print("user =", user)
                else:
                    qr.add_data(f"http://127.0.0.1:8000/create_code/{prymary_key}")
                    print("regular user qrcode creation")
                    image = qr.make_image(
                        fill_color = color,
                        back_color = bg_color
                    )
                
                
                image.save(qrcode_image_path)
                code = Code.objects.create(
                    image_qr = f'{request.user}/{title}.png',
                    title = title,
                    url = url,
                    creator = user,
                    description = description,
                    color = color,
                    bgcolour = bg_color, 
                    costomization = radius,
                    center_image = embaded_img
                )

                cur_code = Code.objects.last()
                cur_date_time = str(cur_code.date_time)
                date_time_change = int(cur_date_time.split(' ')[-1].split(":")[0])+2

                step1 = cur_date_time.split(' ')[0]
                print(step1)
                step2 = cur_date_time.split(":")[1] + ":" + cur_date_time.split(":")[2] + ":" + cur_date_time.split(":")[3]
                print(step2)
                step3 = step1 + " " + str(date_time_change) + ":" + step2
                print(step3)
                code.date_time = step3
                
                if not desktop:
                    # expire_date_list = step1.split("-")
                    expire_date = datetime.datetime.now() + datetime.timedelta(days = 30)
                    print("expire_date =", expire_date)
                    code.expire_date = expire_date
                    # expire_date =  + " " + str(date_time_change) + ":" + step2

                code.save()
                print("code.image_qr =", code.image_qr)
    else:
        number_error = True

    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "code": code,
            'odd_number': number_error,
            # 'no_creation': creation_error,
            "user_status": user_status,
            "is_desktop_mess_error": is_desktop_mess_error,
            "is_not_desktop_mess_error": is_not_desktop_mess_error,
        }
    )


def render_redirect(request: HttpRequest, pk: int):
    # url = request.get_full_path().split("/")[-1]

    code = Code.objects.filter(id = pk)[0]

    expire_date = datetime.datetime.now(datetime.timezone.utc)

    code_url = code.url
    if expire_date <= code.expire_date:
        # print("url =", url)
        return redirect(code_url)
    else:
        return HttpResponse("Срок дії кода вичерпано")
        # return HttpResponse(f"Redirection {code_url, code.expire_date, expire_date}")