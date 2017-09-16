from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.LoginView.as_view(extra_context={'next': '/'})),
    url(r'^logged_out$', views.did_loggout),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(next_page='/logged_out')),
    url(r'accounts/create/$', views.create_account),
    url(r'$', views.test)
]