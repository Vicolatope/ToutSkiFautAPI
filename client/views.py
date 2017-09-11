from django.shortcuts import render

# Create your views here.

def did_loggout(request):
    return render(request, 'logout.html')
