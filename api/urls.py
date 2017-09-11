from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^rentitem/', views.RentItemView.as_view()),
]