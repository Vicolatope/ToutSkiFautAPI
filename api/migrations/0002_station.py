# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=12)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=12)),
            ],
        ),
    ]
