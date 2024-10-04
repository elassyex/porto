from django.shortcuts import render, HttpResponse
import requests
from .models import Ips
import porto.settings as settings
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import BaseDetailView

def resum(request):
    with open(settings.STATIC_ROOT / 'myresume.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed

def home(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    # device_type = ""
    # browser_type = ""
    # browser_version = ""
    # os_type = ""
    # os_version = ""
    # if request.user_agent.is_mobile:
    #     device_type = "Mobile"
    # if request.user_agent.is_tablet:
    #     device_type = "Tablet"
    # if request.user_agent.is_pc:
    #     device_type = "PC"
    
    # browser_type = request.user_agent.browser.family
    # browser_version = request.user_agent.browser.version_string
    # os_type = request.user_agent.os.family
    # os_version = request.user_agent.os.version_string
    # response = requests.get(f'https://ipapi.co/{ip}/json/').json()

    # cx = Ips(
    #     ip = ip,
    #     dev = device_type,
    #     browser = browser_type,
    #     so = os_type,
    #     city= response.get("city"),
    #     region= response.get("region"),
    #     country= response.get("country_name")
    # )
    # cx.save()
    # context = {
    #     "ip": ip,
    #     "device_type": device_type,
    #     "browser_type": browser_type,
    #     "browser_version": browser_version,
    #     "os_type":os_type,
    #     "os_version":os_version
    # }
    return render(request, 'base/index.html')

def home2(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    # device_type = ""
    # browser_type = ""
    # browser_version = ""
    # os_type = ""
    # os_version = ""
    # if request.user_agent.is_mobile:
    #     device_type = "Mobile"
    # if request.user_agent.is_tablet:
    #     device_type = "Tablet"
    # if request.user_agent.is_pc:
    #     device_type = "PC"
    
    # browser_type = request.user_agent.browser.family
    # browser_version = request.user_agent.browser.version_string
    # os_type = request.user_agent.os.family
    # os_version = request.user_agent.os.version_string
    # response = requests.get(f'https://ipapi.co/{ip}/json/').json()

    # cx = Ips(
    #     ip = ip,
    #     dev = device_type,
    #     browser = browser_type,
    #     so = os_type,
    #     city= response.get("city"),
    #     region= response.get("region"),
    #     country= response.get("country_name")
    # )
    # cx.save()
    # context = {
    #     "ip": ip,
    #     "device_type": device_type,
    #     "browser_type": browser_type,
    #     "browser_version": browser_version,
    #     "os_type":os_type,
    #     "os_version":os_version
    # }
    return render(request, 'base/index2.html')


