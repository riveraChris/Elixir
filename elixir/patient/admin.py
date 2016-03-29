from django.contrib import admin

from .models import Patient, Record, Note

admin.site.register(Patient)
admin.site.register(Record)
admin.site.register(Note)