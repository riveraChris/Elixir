from __future__ import unicode_literals
from doctor.models import Doctor
from appointment.models import Appointment
from record.models import Record
from django.db import models
from timezone_field import TimeZoneField


class Patient(models.Model):
	name = models.CharField(max_length = 30, default = '')
	mid_name = models.CharField(max_length = 1, blank=True, null=True)
	first_last_name = models.CharField(max_length = 30, default = '')
	second_last_name = models.CharField(max_length = 30, default = '')
	birthdate = models.DateField()
	age = models.PositiveIntegerField()
	sex = models.CharField(max_length = 1)
	address1 = models.CharField(max_length = 100)
	address2 = models.CharField(max_length = 100, blank=True, null=True)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 2)
	zipcode = models.PositiveIntegerField()
	phone = models.CharField(max_length = 20, blank=True, null=True)
	doctor = models.ForeignKey(Doctor, blank=True, null=True)
	appointment = models.ForeignKey(Appointment, blank=True, null=True)
	record = models.ForeignKey(Record, blank=True, null=True)

	def get_absolute_url(self):
		return reverse('dash', args=[str(self.id)])