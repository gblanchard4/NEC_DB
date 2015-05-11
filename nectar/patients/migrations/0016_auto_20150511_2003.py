# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_auto_20150511_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='abx',
            field=models.BooleanField(default=False, verbose_name=b'Antibiotics'),
            preserve_default=True,
        ),
    ]
