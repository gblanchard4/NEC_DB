# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0019_auto_20150512_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='stool',
            name='have_extract',
            field=models.BooleanField(default=False, verbose_name=b'Extracted Stool Available'),
        ),
        migrations.AddField(
            model_name='stool',
            name='have_raw',
            field=models.BooleanField(default=False, verbose_name=b'Raw Stool Available'),
        ),
    ]
