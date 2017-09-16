from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    url(r'token/obtain/', obtain_auth_token),
    url(r'^accounts/create', views.create_account),
    url(r'logged_out', views.did_loggout),
]