from __future__ import unicode_literals
from doctor.models import Doctor
from django.db import models

class Patient(models.Model):
	name = models.CharField(max_length = 30, default = 'unknown')
	mid_name = models.CharField(max_length = 1)
	first_last_name = models.CharField(max_length = 30, default = 'unknown')
	second_last_name = models.CharField(max_length = 30, default = 'unknown')
	birthdate = models.DateField(auto_now_add = True)
	age = models.PositiveIntegerField()
	sex = models.CharField(max_length = 1)
	height = models.FloatField()
	wheight = models.FloatField()
	address1 = models.CharField(max_length = 100)
	address2 = models.CharField(max_length = 100)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 2)
	zipcode = models.PositiveIntegerField()

	doctor = models.ManyToManyField(Doctor)
