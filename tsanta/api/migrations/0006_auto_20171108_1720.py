# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171108_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='social_network_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
