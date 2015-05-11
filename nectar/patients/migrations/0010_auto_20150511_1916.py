# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_auto_20150511_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=b'N', max_length=1, verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female'), (b'N', b'Not Set')]),
        ),
        migrations.AlterField(
            model_name='environment',
            name='sequence_available',
            field=models.BooleanField(default=False, verbose_name=b'Sequence Available'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='bollus_cont',
            field=models.CharField(max_length=1, verbose_name=b'Bollus Continuous', choices=[(b'B', b'Bolus'), (b'C', b'Cont')]),
        ),
        migrations.AlterField(
            model_name='stool',
            name='indometh',
            field=models.BooleanField(default=False, verbose_name=b'Indomethacin'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='pneumo',
            field=models.DateField(help_text=b'Date of onset, leave blank if none', null=True, verbose_name=b'Pneumatosis Intestinalis', blank=True),
        ),
    ]
