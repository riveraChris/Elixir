from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from doctor.models import Doctor
from appointment.models import Appointment
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime

from django.db import models


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
	doctor = models.ForeignKey(Doctor)
	

	def get_absolute_url(self):
		return reverse('update_record', args=[str(self.id)])

	def __str__(self):
		return self.name + ' ' + self.first_last_name

def record_save(sender, instance, created, *args, **kwargs):
	patient = instance
	new_rec = Record()
	new_rec.patient = patient
	new_rec.save()

post_save.connect(record_save, sender = Patient)
	
class Note(models.Model):
	created_by = models.CharField(max_length = 30)
	created_dt = models.DateField()
	created_tm = models.TimeField()
	received_Place = models.CharField(max_length = 30, default = '')
	received_State = models.CharField(max_length = 30, default = '')
	service_Food = models.CharField(max_length = 30, default = '')
	returned_Type = models.CharField(max_length = 30, default = '')
	diaper = models.CharField(max_length = 10, blank=True, null=True)
	evacuations = models.CharField(max_length = 10, blank=True, null=True)
	milk = models.CharField(max_length = 10, blank=True, null=True)
	snack = models.CharField(max_length = 10, blank=True, null=True)
	hygiene = models.CharField(max_length = 10, blank=True, null=True)
	comments = models.CharField(max_length = 255, blank=True, null=True)
	
	RECEIVEDPLACE = (
			('Cuarto','Cuarto'),
			('Sala','Sala'),
			('Comedor','Comedor'),
			('Area de Juegos','Area de Juegos'),
		)
	RECEIVEDSTATE = (
			('Dormido','Dormido'), 
			('Despierto','Despierto'),
		)
	SERVICEFOOD = (
			('Desayuno','Desayuno'),
			('Almuerzo','Almuerzo'),
			('Cena','Cena'),
		)

class Record(models.Model):
	patient = models.OneToOneField(Patient)
	medical_plan_name = models.CharField(max_length = 30, blank=True, null=True)
	medical_plan_number = models.CharField(max_length = 30, blank=True, null=True)
	height = models.FloatField(blank=True, null=True)
	weight = models.FloatField(blank=True, null=True)
	condition_1 = models.CharField(max_length = 30, blank=True, null=True)
	condition_2 = models.CharField(max_length = 30, blank=True, null=True)
	condition_3 = models.CharField(max_length = 30, blank=True, null=True)
	more_info = models.CharField(max_length = 255, blank=True, null=True)
	appointment = models.ForeignKey(Appointment, blank=True, null=True)
	note = models.ForeignKey(Note, blank=True, null=True)
	created_By = models.ForeignKey(User, related_name = 'user', blank=True, null=True)
	created_DT = models.DateField(default = datetime.date.today(), blank=True, null=True)
	modified_By = models.ForeignKey(User, blank=True, null=True)
	modified_DT = models.DateField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse('update_record', args=[str(self.id)])
		
	def __str__(self):
		return 'Record Number {0}'.format(self.id)