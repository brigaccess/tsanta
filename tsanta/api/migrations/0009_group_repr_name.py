# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20171118_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='repr_name',
            field=models.CharField(default='', max_length=503),
            preserve_default=False,
        ),
    ]
