from __future__ import unicode_literals
from treatment.models import Treatment
from django.db import models

class Appointment(models.Model):
	date = models.DateField(auto_now_add = True, null = True)
	treatment = models.ForeignKey(Treatment)