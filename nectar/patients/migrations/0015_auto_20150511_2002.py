# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_auto_20150511_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='abx_notes',
            field=models.TextField(default=b'', verbose_name=b'Antibiotics Notes', blank=True),
            preserve_default=True,
        ),
    ]
