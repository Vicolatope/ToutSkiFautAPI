from rest_framework import serializers
from .models import RentItem
import json

class RentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItem
        fields = ('id', 'begin_disp', 'end_disp', 'added', 'name', 'description', 'brand', 'type', 'disabled')