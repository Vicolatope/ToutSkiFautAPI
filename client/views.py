from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import User
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log_user

import pendulum
import traceback

# Create your views here.

def did_loggout(request):
    return render(request, 'logout.html')

def test(request):
	users = []
	for u in User.objects.all():
		users.append([u.username, u.email, u.password])
	return JsonResponse(users, safe=False)

def my_profile(request):
    print(request.user)
    if (request.user.is_anonymous()):
        return render(request, 'home.html')
    return render(request, 'profile.html')

@csrf_exempt
def logout_user(request):
    logout(request)
    return render(request, 'home.html')

@csrf_exempt
def login(request):
    users = []
    for u in User.objects.all():
        users.append([u.username, u.email, u.password])
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        log_user(request, user)
        return HttpResponse('ok')
    else:
        return HttpResponse('wrong credentials')
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def create_account(request):
    # try:
    print(request.POST['username'])
    if len(User.objects.filter(username=request.POST['username'])):
        return HttpResponse('Cet utilistaeur existe déjà', status=HTTP_400_BAD_REQUEST)
    birthdate = pendulum.parse(request.POST['birthdate'])
    User.objects.create_user(
        request.POST['username'],
        request.POST['username'],
        request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        )
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    user.birth_date = birthdate
    user.save()
    log_user(request, user)
    return HttpResponse('user created')
    # except Exception as e:
    #     print(e)
    #     return HttpResponse('Adresse email invalide', status=status.HTTP_400_BAD_REQUEST)

def home_page(request):
    print(request.user)
    return render(request, 'home.html')