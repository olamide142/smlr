from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . models import *
# Create your views here.








@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        'Login' : 'api/login',
        'Registration' : 'api/registration',
        'Dashboard' : '/api/dashboard',
        'Get Smlr' : '/api/getSmlr',
    }
    return Response(api_urls)



@api_view(["POST"])
def apiRegistration(request):
    validate_what = request.POST.get('validate_what')

    # Username Verification
    if(validate_what == 'username'):
        username = request.POST.get('username')
        user = User.objects.filter(username=username).exists()
        if user:
            # username already exist
            return Response({'color':'red'})
        else:
            return Response({'color':'green'})

    # Phone Number Verification
    # elif  (validate_what == 'email'):
    #     email = request.POST.get('email')
    #     user = Diary.objects.filter(email=email).exists()

    #     if user:
    #         return Response({'color': 'red'})
    #     else:
    #         return Response({'color': 'green'})

    # Register new user
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        # log user in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if user exist
            # Allocate_diary_to_new_user
            user = User.objects.get(username=username)
            dashnoard = Dashboard.objects.create(dashboard_id=randomId(), owner=user)
            dashnoard.save()
            return Response({'status': 'success'})



@api_view(["POST"])
def apiLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        context = {'status': 'true', 'dashboard_id' : ''}
        return Response(context)
    else:
        context = {'status': 'false'}
        return Response(context)



@api_view(["POST"])
def apigetSmlr(request):
    destination = request.POST.get('destination')
    if ("http://" or "https://") not in str(destination):
        destination = "http://"+str(destination)
    
    if request.user.is_authenticated:
        smlr = SmlrUrl.objects.create(smlr_url_id=randomId(), owner=request.user.username, destination_url=destination)
    else:
        smlr = SmlrUrl.objects.create(smlr_url_id=randomId(), owner="AnonymousUser", destination_url=destination)
    
    smlr.save()
    context = {'smlr_url':smlr.smlr_url_id}
    return Response(context)



@api_view(["GET"])
def apiDashBoard(request):
    
    return Response()


    
#
#
# @api_view(["GET"])
# def taskList(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
#
# @api_view(["GET"])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = TaskSerializer(tasks, many=False)
#     return Response(serializer.data)
#
# @api_view(["POST"])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response("Success")
#
#
# @api_view(["POST"])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response("Success")
#
#
# @api_view(["DELETE"])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return Response("Success")
#
