# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=30)),
                ('mid_name', models.CharField(max_length=1, null=True)),
                ('first_last_name', models.CharField(default='unknown', max_length=30)),
                ('second_last_name', models.CharField(default='unknown', max_length=30)),
                ('age', models.PositiveIntegerField(null=True)),
                ('sex', models.CharField(max_length=1, null=True)),
                ('address1', models.CharField(max_length=100, null=True)),
                ('address2', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('zipcode', models.PositiveIntegerField(null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
