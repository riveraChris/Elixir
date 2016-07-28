from __future__ import unicode_literals

from django.db import models

class Doctor(models.Model):
	name = models.CharField(max_length = 30, default = '')
	mid_name = models.CharField(max_length = 1, blank=True, null = True)
	first_last_name = models.CharField(max_length = 30, default = '')
	second_last_name = models.CharField(max_length = 30, default = '')
	age = models.PositiveIntegerField(blank=True, null=True)
	sex = models.CharField(max_length = 1, null = True)
	address1 = models.CharField(max_length = 100, blank=True, null=True)
	address2 = models.CharField(max_length = 100, blank=True, null=True)
	city = models.CharField(max_length = 30, blank=True, null=True)
	state = models.CharField(max_length = 2, blank=True, null=True)
	zipcode = models.PositiveIntegerField(blank=True, null=True)
	phone = models.CharField(max_length = 20, blank=True, null=True)
	specialist = models.CharField(max_length = 20, blank=True, null=True)
	
	def __str__(self):
		return self.name + ' ' + self.first_last_name