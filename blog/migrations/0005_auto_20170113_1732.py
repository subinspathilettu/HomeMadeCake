# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170113_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(upload_to='/Users/subins/Desktop/HomeMadeCake/media'),
        ),
    ]