# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160413_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]