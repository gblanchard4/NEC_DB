# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0023_patient_nec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='uvva',
            field=models.BooleanField(default=False, verbose_name=b'UV/VA'),
        ),
    ]
