from django.contrib import admin

from .models import Patient, Stool, Environment
# from .models import Stool
# from .models import Environment

class PatientAdmin(admin.ModelAdmin):
	list_display = ('patientid', 'dob', 'gestational_age', 'birth_weight')

class StoolAdmin(admin.ModelAdmin):
	list_display = ('patient', 'date', 'dol')

class EnvironmentAdmin(admin.ModelAdmin):
	list_display = ('patientid', 'date', 'room')

# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(Stool, StoolAdmin)
admin.site.register(Environment, EnvironmentAdmin)

