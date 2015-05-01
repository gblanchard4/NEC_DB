# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='neg_pressure',
            field=models.BooleanField(default=True, verbose_name=b'Negative Pressure'),
        ),
        migrations.AlterField(
            model_name='environment',
            name='sequence_available',
            field=models.BooleanField(default=True, verbose_name=b'Sequece Available'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='delivery',
            field=models.CharField(max_length=1, verbose_name=b'Delivery Method', choices=[(b'C', b'Cesarean '), (b'V', b'Vaginal')]),
        ),
        migrations.AlterField(
            model_name='stool',
            name='caffeine',
            field=models.BooleanField(default=True, verbose_name=b'Caffeine'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='full_feed',
            field=models.BooleanField(default=True, verbose_name=b'Full Feed'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='h2block',
            field=models.BooleanField(default=True, verbose_name=b'H2 Blockers'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='indometh',
            field=models.BooleanField(default=True, verbose_name=b'Indometh'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='nec',
            field=models.BooleanField(default=True, verbose_name=b'NEC'),
        ),
    ]
