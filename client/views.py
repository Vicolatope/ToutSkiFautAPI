from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def did_loggout(request):
    return render(request, 'logout.html')

def test(request):
	users = []
	for u in User.objects.all():
		users.append([u.username, u.email, u.password])
	return JsonResponse(users, safe=False)

@csrf_exempt
def create_account(request):
    try:
        User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
        return HttpResponse('user created')
    except:
        return HttpResponse('not created', status=status.HTTP_400_BAD_REQUEST)