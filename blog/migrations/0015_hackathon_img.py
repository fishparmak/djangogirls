# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-11 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_team_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='img',
            field=models.CharField(default='../media/hack.jpg', max_length=300),
        ),
    ]
