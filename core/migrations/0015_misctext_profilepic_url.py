# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170909_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='misctext',
            name='profilepic_url',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
