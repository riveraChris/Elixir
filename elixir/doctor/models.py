from __future__ import unicode_literals

from django.db import models

class Doctor(models.Model):
	name = models.CharField(max_length = 30, default = 'unknown')
