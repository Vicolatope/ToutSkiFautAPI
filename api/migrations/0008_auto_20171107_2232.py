# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171107_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentitem',
            name='brand',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rentitem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
