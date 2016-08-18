# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_DT',
            field=models.DateField(default=datetime.date(2016, 8, 9), null=True, blank=True),
        ),
    ]
