# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-11 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_hackathon_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='img',
            field=models.CharField(default='../media/org.jpg', max_length=300),
        ),
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.CharField(default='../media/proj.jpg', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.CharField(default='../media/user.jpg', max_length=300),
        ),
    ]
