from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions

from .serializers import RentItemSerializer
from .models import RentItem

from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.decorators import protected_resource


# ================================= Location management View ================================= #

class RentItemView(ProtectedResourceView):
    def post(self, request):
        """Create a new RentItem"""
        serializer = RentItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        try:
            item = RentItem.objects.get(id=item_id)
        except RentItem.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        for field, value in request.data.items():
            if not hasattr(item, field):
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            setattr(item, field, value)
        item.save(update_fields=request.data.keys())
        srlz = RentItemSerializer(item)
        return Response(srlz.data)

    def delete(self, request):
        try:
            item = RentItem.objects.get(id=item_id)
        except RentItem.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        item.disabled = True
        item.save(update_fields=['disabled'])
        srlz = RentItemSerializer(item)
        return Response(srlz.data)

    def get(self, request):
        """List all rentitems"""
        items = RentItem.objects.all()
        serializer = RentItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)


# /location/(item_id)
