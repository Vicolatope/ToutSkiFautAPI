# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentitem',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rentitem',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
