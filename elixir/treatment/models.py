from __future__ import unicode_literals

from django.db import models

class Treatment(models.Model):
	treatment = models.CharField(max_length = 255, null = True)

		
