# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='sex',
            field=models.BooleanField(default=False),
        ),
    ]
