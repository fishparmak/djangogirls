# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-30 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181030_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='seat_id',
        ),
    ]
