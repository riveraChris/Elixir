# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('treatment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('time', models.DateTimeField()),
                ('time_zone', timezone_field.fields.TimeZoneField(default='America/Puerto_Rico')),
                ('task_id', models.CharField(blank=True, editable=False, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('treatment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatment.Treatment')),
            ],
        ),
    ]
