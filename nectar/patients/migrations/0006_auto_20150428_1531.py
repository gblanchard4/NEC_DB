# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20150428_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='pneumo',
            field=models.DateField(help_text=b'Date of onset, leave blank if none', null=True, verbose_name=b'Pnuemonia', blank=True),
        ),
    ]
