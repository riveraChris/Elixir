# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 01:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        ('doctor', '0002_auto_20160224_0102'),
        ('record', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='wheight',
        ),
        migrations.AddField(
            model_name='patient',
            name='appointment',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.CASCADE, to='appointment.Appointment'),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='record',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.CASCADE, to='record.Record'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zipcode',
            field=models.PositiveIntegerField(null=True),
        ),
    ]