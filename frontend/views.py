from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import *
from django.contrib.auth import authenticate, login, logout
from api.models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def indexView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'frontend/index.html')

# @login_required(login_url="/")
def dashboardView(request):
    return render(request, 'frontend/dashboard.html')

def routeView(request, smlr_url):
    try:
        smlr = SmlrUrl.objects.get(smlr_url_id = smlr_url)
        return redirect(str(smlr.destination_url))
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')

def logoutView(request):
    logout(request)
    return redirect('index')

    

