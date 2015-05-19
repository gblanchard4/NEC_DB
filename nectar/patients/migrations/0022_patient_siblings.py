# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_auto_20150512_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='siblings',
            field=models.ManyToManyField(related_name='siblings_rel_+', verbose_name=b'Siblings', to='patients.Patient', blank=True),
        ),
    ]
