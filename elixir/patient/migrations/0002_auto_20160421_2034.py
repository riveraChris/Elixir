# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 20:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_DT',
            field=models.DateField(blank=True, default=datetime.date(2016, 4, 21), null=True),
        ),
    ]
