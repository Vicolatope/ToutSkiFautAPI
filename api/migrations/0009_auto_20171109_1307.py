# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20171107_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('address_comp', models.CharField(max_length=255, null=True)),
                ('addr_city', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=10)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RentItem')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='addr_city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_comp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]