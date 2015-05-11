# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20150511_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='stool',
            name='abx_notes',
            field=models.TextField(default=b'', verbose_name=b'Antibiotics Notes'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='abx',
            field=models.BooleanField(verbose_name=b'Antibiotics'),
        ),
    ]
