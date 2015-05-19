# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_patient_siblings'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nec',
            field=models.BooleanField(default=False, verbose_name=b'NEC'),
        ),
    ]
