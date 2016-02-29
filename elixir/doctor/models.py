from __future__ import unicode_literals

from django.db import models

class Doctor(models.Model):
	name = models.CharField(max_length = 30, default = 'unknown')
	mid_name = models.CharField(max_length = 1, null = True)
	first_last_name = models.CharField(max_length = 30, default = 'unknown')
	second_last_name = models.CharField(max_length = 30, default = 'unknown')
	age = models.PositiveIntegerField(null = True)
	sex = models.CharField(max_length = 1, null = True)
	address1 = models.CharField(max_length = 100, null = True)
	address2 = models.CharField(max_length = 100, null = True)
	city = models.CharField(max_length = 50, null = True)
	state = models.CharField(max_length = 2, null = True)
	zipcode = models.PositiveIntegerField(null = True)
	phone = models.CharField(max_length = 20, null = True)
	
