from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions

from .serializers import RentItemSerializer
from .models import RentItem

from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView

from .constants import db_credentials

import psycopg2

import json

# ================================= Location management View ================================= #

@api_view(['GET'])
def rent_item_detail(request, pk):
    print(pk, type(pk))
    try:
        rent_item = RentItem.objects.get(id=int(pk))
        print(rent_item.name)
    except RentItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    srlz = RentItemSerializer(rent_item)
    return Response({'rentitem': srlz.data})


class RentItemList(APIView):
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

        return Response({'rentitem': serializer.data})

@api_view(['GET'])
def get_all_known_items(request, type, year):
    with psycopg2.connect(db_credentials) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    brand_name,
                    ARRAY_AGG(model_name)
                 from ski_brands SB
                    join ski_items SI
                    ON SI.brand_id = SB.id
                    WHERE SI.model_year = 2012
                    group by brand_name
                """, {'year': year})
            res = {el[0]: el[1] for el in cur.fetchall()}
            return JsonResponse(res, safe=False)


# /location/(item_id)
