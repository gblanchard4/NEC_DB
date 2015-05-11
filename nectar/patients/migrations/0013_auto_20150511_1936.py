# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20150511_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='bollus_cont',
            field=models.CharField(max_length=1, verbose_name=b'Bollus Continuous', choices=[(b'B', b'Bolus'), (b'C', b'Cont'), (b'N', b'None')]),
        ),
    ]
