# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 13:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 5, 38, 28, 615000)),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 5, 38, 28, 615000)),
        ),
    ]