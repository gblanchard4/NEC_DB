# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_auto_20150511_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='freezer_location',
        ),
        migrations.AddField(
            model_name='environment',
            name='box',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'Box Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='environment',
            name='rack',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'Rack Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AddField(
            model_name='environment',
            name='shelf',
            field=models.CharField(default=b'0', max_length=2, verbose_name=b'Shelf Location'),
        ),
    ]
