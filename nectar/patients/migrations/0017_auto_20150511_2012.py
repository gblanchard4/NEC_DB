# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0016_auto_20150511_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='stool',
            name='sequence_available',
            field=models.BooleanField(default=False, verbose_name=b'Sequence Available'),
        ),
        migrations.AddField(
            model_name='stool',
            name='sequence_file',
            field=models.CharField(max_length=60, verbose_name=b'Sequece File Name', blank=True),
        ),
        migrations.AlterField(
            model_name='environment',
            name='sequence_file',
            field=models.CharField(max_length=60, verbose_name=b'Sequece File Name', blank=True),
        ),
    ]
