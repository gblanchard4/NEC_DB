# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20150428_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='weight_gestational_age_aprop',
            field=models.CharField(max_length=7, verbose_name=b'Gestational Weight Age Appropriate', choices=[(b'AGA', b'AGA'), (b'LGA', b'LGA'), (b'SGA', b'SGA'), (b'SGAIUGR', b'SGA/IUGR')]),
        ),
    ]
