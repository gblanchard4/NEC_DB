from django.contrib import admin
from .models import Patient, Stool, Environment

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patientid', 'dob', 'gestational_age', 'birth_weight')
    fieldsets = (
        (None, {
            'fields': ['patientid', 'dob', 'gender', 'race']
        }),
        (None, {
            'fields':[('birth_weight', 'gestational_age', 'weight_gestational_age_aprop'),
                        'delivery', ('apgar_1','apgar_2'),'resusc','rom',('matHX','matMed')]
        })
    )


class StoolAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'dol')
    fieldsets = (
        ('Sample Information', {
            'fields':['patient', 'date', 'nec', 'uvva', 'pneumo']
        }),
        ('Nutrition', {
            'fields':[('feeds', 'full_feed'), 'bollus_cont']
        }),
        ('Medications', {
            'fields':[('h2block', 'indometh', 'caffeine'), ('abx', 'abx_notes')]
        }),
        ('Raw Sample',{
            'fields':[('have_raw', 'raw_shelf', 'raw_rack', 'raw_box')]
        }),
        ('Extracted Sample',{
            'fields':[('have_extract', 'extract_shelf', 'extract_rack', 'extract_box')]
        }),
        ('Sequence Information',{
            'fields':['sequence_available', 'sequence_file']
        })
    )

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('patientid', 'date', 'room')
    fieldsets = (
        (None,  {
                'fields': [('patientid')]
        }),
        ('Sample Information', {
                'fields':['date','crib','room','neg_pressure']
        }),
        ('Sample Location', {
                'fields':[('shelf','rack','box')]
        }),
        ('Sequence Information', {
            'fields':[('sequence_available','sequence_file')]
        })
    )

# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(Stool, StoolAdmin)
admin.site.register(Environment, EnvironmentAdmin)

