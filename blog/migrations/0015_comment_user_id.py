# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160418_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]