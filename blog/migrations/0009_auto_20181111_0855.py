# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-11 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181111_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='level',
        ),
        migrations.AddField(
            model_name='userrole',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Level'),
        ),
    ]
