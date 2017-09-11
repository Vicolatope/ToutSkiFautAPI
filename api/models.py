from __future__ import unicode_literals

from django.db import models

# Create your models here.

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
    brand = models.IntegerField()
    type = models.IntegerField()
    begin_disp = models.DateField()
    end_disp = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
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
