from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^rentitems', views.RentItemView.as_view()),
]