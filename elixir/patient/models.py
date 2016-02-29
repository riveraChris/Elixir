from __future__ import unicode_literals
from doctor.models import Doctor
from appointment.models import Appointment
from record.models import Record
from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length = 30, default = 'unknown')
	mid_name = models.CharField(max_length = 1)
	first_last_name = models.CharField(max_length = 30, default = 'unknown')
	second_last_name = models.CharField(max_length = 30, default = 'unknown')
	birthdate = models.DateField(auto_now_add = True)
	age = models.PositiveIntegerField(null = True)
	sex = models.CharField(max_length = 1)
	address1 = models.CharField(max_length = 100, null = True)
	address2 = models.CharField(max_length = 100, null = True)
	city = models.CharField(max_length = 50, null = True)
	state = models.CharField(max_length = 2, null = True)
	zipcode = models.PositiveIntegerField(null = True)
	phone = models.CharField(max_length = 20, null = True)
	doctor = models.ForeignKey(Doctor, default = '-1')
	appointment = models.ForeignKey(Appointment, default = '-1')
	record = models.ForeignKey(Record, default = '-1')