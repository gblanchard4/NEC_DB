# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20150427_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='neg_pressure',
            field=models.BooleanField(default=False, verbose_name=b'Negative Pressure'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='environment',
            name='sequence_available',
            field=models.BooleanField(default=False, verbose_name=b'Sequece Available'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stool',
            name='caffeine',
            field=models.BooleanField(default=False, verbose_name=b'Caffeine'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stool',
            name='full_feed',
            field=models.BooleanField(default=False, verbose_name=b'Full Feed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stool',
            name='h2block',
            field=models.BooleanField(default=False, verbose_name=b'H2 Blockers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stool',
            name='indometh',
            field=models.BooleanField(default=False, verbose_name=b'Indometh'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stool',
            name='nec',
            field=models.BooleanField(default=False, verbose_name=b'NEC'),
            preserve_default=True,
        ),
    ]
