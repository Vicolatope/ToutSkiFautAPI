from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(User):
    birthdate = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=True)
    address_comp = models.CharField(max_length=255, null=True)
    addr_city = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=10, null=True)


class Address(models.Model):
    address = models.CharField(max_length=255)
    address_comp = models.CharField(max_length=255, null=True)
    addr_city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    item_id = models.ForeignKey('RentItem', on_delete=models.CASCADE)    

class Renting(models.Model):
    """Rented item
    -item_id: the rented item
    -end/begin_date: the rent period
    -rented_to: user who rented the item"""

    item_id = models.IntegerField()
    begin_date = models.DateField()
    end_date = models.DateField()

class RentItem(models.Model):
    """Item for rent:
    -name: item name
    -brand: item's brand id
    -type: item's type
    -begin/end_disp: Beginning and end of rent period
    -added: date item was added
    -descrition: item's description
    -disabled: item's availability"""

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.IntegerField()
    user = models.IntegerField()
    begin_disp = models.DateField(null=True)
    end_disp = models.DateField(null=True)
    quality = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(null=True)
    size_unit = models.CharField(max_length=5, null=True)
    description = models.CharField(max_length=255, null=True)
    disabled = models.BooleanField(default=False)


class Station(models.Model):
    """Ski station
    -name: station's name
    -lat/lon: gps for map positioning"""
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=12, decimal_places=10)
    lon = models.DecimalField(max_digits=12, decimal_places=10)


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
