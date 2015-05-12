# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0018_auto_20150512_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='stool',
            name='extract_box',
            field=models.IntegerField(default=b'0', verbose_name=b'Extracted Stool Box Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='stool',
            name='extract_rack',
            field=models.IntegerField(default=b'0', verbose_name=b'Extracted Stool Rack Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='stool',
            name='extract_shelf',
            field=models.IntegerField(default=b'0', verbose_name=b'Extracted Stool Shelf Location'),
        ),
        migrations.AddField(
            model_name='stool',
            name='raw_box',
            field=models.IntegerField(default=b'0', verbose_name=b'Raw Stool Box Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='stool',
            name='raw_rack',
            field=models.IntegerField(default=b'0', verbose_name=b'Raw Stool Rack Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='stool',
            name='raw_shelf',
            field=models.IntegerField(default=b'0', verbose_name=b'Raw Stool Shelf Location'),
        ),
    ]
