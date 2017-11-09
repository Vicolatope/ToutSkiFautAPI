from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'token/obtain/', obtain_auth_token),
    url(r'^accounts/create', views.create_account),
    url(r'^accounts/login', views.login),
    url(r'^accounts/logging_out', views.logout_user),
    url(r'logged_out', views.did_loggout),
    url(r'add_item', TemplateView.as_view(template_name="add_item.html")),
    url(r'^profile$', views.my_profile),
    url(r'', views.home_page),
]