# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0024_auto_20150519_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='box',
            field=models.CharField(max_length=30, verbose_name=b'Box Location'),
        ),
        migrations.AlterField(
            model_name='environment',
            name='rack',
            field=models.CharField(max_length=30, verbose_name=b'Rack Location'),
        ),
        migrations.AlterField(
            model_name='environment',
            name='shelf',
            field=models.CharField(max_length=30, verbose_name=b'Shelf Location'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='extract_box',
            field=models.CharField(max_length=30, verbose_name=b'Extracted Stool Box Location'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='extract_rack',
            field=models.CharField(max_length=30, verbose_name=b'Extracted Stool Rack Location'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='extract_shelf',
            field=models.CharField(max_length=30, verbose_name=b'Extracted Stool Shelf Location'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='raw_box',
            field=models.CharField(max_length=30, verbose_name=b'Raw Stool Box Location'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='raw_rack',
            field=models.CharField(max_length=30, verbose_name=b'Raw Stool Rack Location'),
        ),
        migrations.AlterField(
            model_name='stool',
            name='raw_shelf',
            field=models.CharField(max_length=30, verbose_name=b'Raw Stool Shelf Location'),
        ),
    ]
