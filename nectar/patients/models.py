from django.db import models
from datetime import datetime

# Create your models here.
class Patient(models.Model):

    #Choices for fields
    RACE_CHOICES = (
        ('B', 'Black'),
        ('W', 'White'),
        ('H', 'Hispanic'),
        ('A', 'Asian'),
        ('I', 'Indian')
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Set')
    )

    GESTATIONAL_APROP_CHOICES = (
        ('AGA', 'AGA'),
        ('LGA', 'LGA'),
        ('SGA', 'SGA'),
        ('SGAIUGR', 'SGA/IUGR')
    )

    DELIVERY_CHOICES = (
        ('C', 'Cesarean '),
        ('V', 'Vaginal')
    )

    RESUSC_CHOICES = (
        ('I', 'Intibition'),
        ('P', 'Positive Pressure'),
        ('B','Bagged Oxygen'),
        ('N', 'None')
    )

    APGAR_CHOICES = zip( range(0,10), range(0,10))



    patientid = models.CharField(primary_key=True, max_length=30, verbose_name="Patient ID")
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gender', default='N' )
    race = models.CharField(max_length=1, choices=RACE_CHOICES, verbose_name="Race")
    gestational_age = models.IntegerField(verbose_name="Gestational Age")
    birth_weight = models.IntegerField(verbose_name="Birth Weight")
    weight_gestational_age_aprop = models.CharField(max_length=7, choices=GESTATIONAL_APROP_CHOICES, verbose_name="Gestational Weight Age Appropriate")
    delivery = models.CharField(max_length=1, choices=DELIVERY_CHOICES , verbose_name="Delivery Method")
    apgar_1 = models.IntegerField(choices=APGAR_CHOICES, verbose_name="Apgar Score 1st Number")
    apgar_2 = models.IntegerField(choices=APGAR_CHOICES, verbose_name="Apgar Score 2nd Number")
    resusc = models.CharField(max_length=1, choices=RESUSC_CHOICES, verbose_name="Resuscitation")
    rom = models.IntegerField(verbose_name="ROM in Hours")
    matHX = models.CharField(max_length=200, verbose_name="Maternal HX")
    matMed = models.CharField(max_length=200, verbose_name="Maternal Medicine")
 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.patientid)

class Stool(models.Model):

    UVVA_CHOICES = (
        ('N','None'),
        ('UA','UA'),
        ('UV','OV')
    )
    FEEDS_CHOICES = (
        ('F','Formula'),
        ('B','Breast Milk'), 
        ('N', 'NPO'), 
        ('M', 'Mixed')

    )
    BOLLUS_CONT_CHOICES = (
        ('B','Bolus'),
        ('C', 'Cont')
    )
    patient= models.ForeignKey(Patient)
    date =  models.DateField(verbose_name="Sample Date")
    #day_of_life = models.IntegerField(verbose_name="Day of Life", help_text="Calcuated automagically", default=self.dol())
    uvva = models.CharField(max_length=2, choices=UVVA_CHOICES, verbose_name="UV/VA")
    feeds = models.CharField(max_length=1, choices=FEEDS_CHOICES, verbose_name="Feeding")
    pneumo = models.DateField(blank=True, null=True, help_text="Date of onset, leave blank if none", verbose_name="Pneumatosis Intestinalis")
    bollus_cont = models.CharField(max_length=1, choices=BOLLUS_CONT_CHOICES, verbose_name="Bollus Continuous")
    full_feed = models.BooleanField(default=False, verbose_name="Full Feed")
    abx = models.DateField(verbose_name="ABX")
    h2block = models.BooleanField(default=False, verbose_name="H2 Blockers")
    indometh = models.BooleanField(default=False, verbose_name="Indomethacin")
    caffeine = models.BooleanField(default=False, verbose_name="Caffeine")
    nec = models.BooleanField(default=False, verbose_name="NEC")

    def __str__(self):              # __unicode__ on Python 2
        return str(self.patient.patientid+self.date.__str__())

    
    def _get_dol(self):     
        dob  = Patient.objects.get(pk=self.patient).dob
        dol_value = (self.date-dob).days
        return dol_value

    dol = property(_get_dol)

class Environment(models.Model):


    RACK_CHOICES = zip( range(0,5), range(0,5))
    BOX_CHOICES = zip( range(0,5), range(0,5))

    patientid = models.ForeignKey(Patient)
    date =  models.DateField(verbose_name="Sample Date")
    crib = models.CharField(max_length=100, verbose_name="Crib")
    room = models.CharField(max_length=5,verbose_name="Room")
    neg_pressure = models.BooleanField(default=False, verbose_name="Negative Pressure")
    shelf = models.CharField(max_length=2, verbose_name="Shelf Location", default='0')
    rack = models.CharField(max_length=1, choices=RACK_CHOICES, verbose_name="Rack Location", default='0')
    box = models.CharField(max_length=1, choices=BOX_CHOICES, verbose_name="Box Location", default='0')
    sequence_available = models.BooleanField(default=False, verbose_name="Sequence Available")
    sequence_file = models.CharField(max_length=30, verbose_name="Sequece File Name")




