# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Sample Date')),
                ('crib', models.CharField(max_length=100, verbose_name=b'Crib')),
                ('room', models.CharField(max_length=5, verbose_name=b'Room')),
                ('neg_pressure', models.BooleanField(verbose_name=b'Negative Pressure')),
                ('freezer_location', models.CharField(max_length=1, verbose_name=b'Freezer Location', choices=[(b'S', b'Shelf'), (b'R', b'Rack'), (b'B', b'Box')])),
                ('sequence_available', models.BooleanField(verbose_name=b'Sequece Available')),
                ('sequence_file', models.FileField(upload_to=b'', verbose_name=b'Sequece File')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientid', models.CharField(max_length=30, serialize=False, verbose_name=b'Patient ID', primary_key=True)),
                ('dob', models.DateField(verbose_name=b'Date of Birth')),
                ('race', models.CharField(max_length=1, verbose_name=b'Race', choices=[(b'B', b'Black'), (b'W', b'White'), (b'H', b'Hispanic'), (b'A', b'Asian'), (b'I', b'Indian')])),
                ('gestational_age', models.IntegerField(verbose_name=b'Gestational Age')),
                ('birth_weight', models.IntegerField(verbose_name=b'Birth Weight')),
                ('weight_gestational_age_aprop', models.CharField(max_length=7, verbose_name=b'Gestational Weight Age Appropriate', choices=[(b'A', b'A'), (b'AGA', b'AGA'), (b'IUGR', b'IUGR'), (b'L', b'L'), (b'LGA', b'LGA'), (b'S', b'S'), (b'SIUGR', b'S(IUGR)'), (b'SGA', b'SGA'), (b'SGAIUGR', b'SGA/IUGR')])),
                ('delivery', models.CharField(max_length=1, verbose_name=b'Delivery Method')),
                ('apgar_1', models.IntegerField(verbose_name=b'Apgar Score 1st Number', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('apgar_2', models.IntegerField(verbose_name=b'Apgar Score 2nd Number', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('resusc', models.CharField(max_length=1, verbose_name=b'Resuscitation', choices=[(b'I', b'Intibition'), (b'P', b'Positive Pressure'), (b'B', b'Bagged Oxygen'), (b'N', b'None')])),
                ('rom', models.IntegerField(verbose_name=b'ROM')),
                ('matHX', models.CharField(max_length=200, verbose_name=b'Maternal HX')),
                ('matMed', models.CharField(max_length=200, verbose_name=b'Maternal Medicine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Sample Date')),
                ('day_of_life', models.IntegerField(verbose_name=b'Day of Life')),
                ('uvva', models.CharField(max_length=2, verbose_name=b'UV/VA', choices=[(b'N', b'None'), (b'UA', b'UA'), (b'UV', b'OV')])),
                ('feeds', models.CharField(max_length=1, verbose_name=b'Feeding', choices=[(b'F', b'Formula'), (b'B', b'Breast Milk')])),
                ('pneumo', models.DateField(help_text=b'Date of onset, leave blank if none', verbose_name=b'Pnuemonia', blank=True)),
                ('bollus_cont', models.CharField(max_length=1, verbose_name=b'Bollus/Cont', choices=[(b'B', b'Bolus'), (b'C', b'Cont')])),
                ('full_feed', models.BooleanField(verbose_name=b'Full Feed')),
                ('abx', models.DateField(verbose_name=b'ABX')),
                ('h2block', models.BooleanField(verbose_name=b'H2 Blockers')),
                ('indometh', models.BooleanField(verbose_name=b'Indometh')),
                ('caffeine', models.BooleanField(verbose_name=b'Caffeine')),
                ('nec', models.BooleanField(verbose_name=b'NEC')),
                ('patientid', models.ForeignKey(to='patients.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='environment',
            name='patientid',
            field=models.ForeignKey(to='patients.Patient'),
            preserve_default=True,
        ),
    ]
