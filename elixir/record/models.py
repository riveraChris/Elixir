from __future__ import unicode_literals

from django.db import models

class Record(models.Model):
	height = models.FloatField()
	wheight = models.FloatField()
	condition_1 = models.CharField(max_length = 30, null = True)
	condition_2 = models.CharField(max_length = 30, null = True)
	condition_3 = models.CharField(max_length = 30, null = True)
	observations = models.CharField(max_length = 255, null = True)
	modified_By = models.PositiveIntegerField()
	modified_DT = models.DateField()
	
class Note(models.Model):
	created_by = models.ForeignKey(Users)
	created_dt = models.DateField()
	created_tm = models.TimeField()
	received_Place = models.CharField(max_length = 30, choices = RECEIVED_PLACE)
	received_State = models.CharField(max_length = 30, choices = RECEIVED_STATE)
	service_Food = models.CharField(max_length = 30, choices = SERVICE_FOOD)
	returned_Type = models.CharField(max_length = 30, choices = RECEIVED_PLACE)
	diaper = models.CharField(max_length = 10, null = True)
	evacuations = models.CharField(max_length = 10, null = True)
	milk = models.CharField(max_length = 10, null = True)
	snack = models.CharField(max_length = 10, null = True)
	hygiene = models.CharField(max_length = 10, null = True)
	comments = models.CharField(max_length = 255, null = True)

	RECEIVED_PLACE = (
		('Cuarto','Cuarto'),
		('Sala','Sala'),
		('Comedor','Comedor'),
		('Area de Juegos','Area de Juegos'),
		)
	RECEIVED_STATE = (
		('Dormido','Dormido'), 
		('Despierto','Despiero'),
		)
	SERVICE_FOOD = (
		('Desayuno','Desayuno'),
		('Almuerzo','Almuerzo'),
		('Cena','Cena'),
		)
