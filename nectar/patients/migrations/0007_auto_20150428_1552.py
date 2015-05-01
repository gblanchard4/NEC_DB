# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20150428_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stool',
            old_name='patientid',
            new_name='patient',
        ),
    ]
