# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170113_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='description',
        ),
        migrations.AddField(
            model_name='cake',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
