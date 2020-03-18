from django.shortcuts import *
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def indexView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'frontend/index.html')

def dashboardView(request):
    if request.user.is_authenticated:
        logged_in_user = User.objects.get(username=str(request.user.username))

        urls = SmlrUrl.objects.filter(owner=logged_in_user)
        stats = Stat.objects.all()

        context = {'urls':urls}
        return render(request, 'frontend/dashboard.html', context)
    else:
        return render(request, 'frontend/index.html')
    

def routeView(request, smlr_url):
    if smlr_url == 'dashboard':
        return render(request, 'frontend/dashboard.html')

    try:
        smlr = SmlrUrl.objects.get(smlr_url_id = smlr_url)
        smlr.visits = F('visits') + 1 
        smlr.save()

        stats = Stat.objects.create(url=smlr_url)
        stats.save()

        return redirect(str(smlr.destination_url))
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')

def logoutView(request):
    logout(request)
    return redirect('index')

    


def apigetSmlr(request):
    destination = request.POST.get('destination')
    if "http" not in str(destination):
        destination = "http://"+str(destination)
    
    if request.user.is_authenticated:
        smlr = SmlrUrl.objects.create(smlr_url_id=randomId(), owner=request.user.username, destination_url=destination)
    else:
        smlr = SmlrUrl.objects.create(smlr_url_id=randomId(), owner="AnonymousUser", destination_url=destination)
    
    smlr.save()
    context = {'smlr_url':smlr.smlr_url_id}
    return JsonResponse(context)


def apiLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        context = {'status': 'true', 'dashboard_id' : ''}
        return JsonResponse(context)
    else:
        context = {'status': 'false'}
        return Response(context)




















