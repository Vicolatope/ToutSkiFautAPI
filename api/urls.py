from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^rentitems$', views.RentItemList.as_view()),
    url(r'^rentitem/add', views.add_new_item),
    url(r'^rentitems/(?P<pk>[\d]+)$', views.rent_item_detail),
    url(r'^all_items/([\d])/([\d]+)$', views.get_all_known_items)
]