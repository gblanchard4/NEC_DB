# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20150511_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='box',
            field=models.IntegerField(default=b'0', verbose_name=b'Box Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='environment',
            name='rack',
            field=models.IntegerField(default=b'0', verbose_name=b'Rack Location', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='environment',
            name='shelf',
            field=models.IntegerField(default=b'0', verbose_name=b'Shelf Location'),
            preserve_default=True,
        ),
    ]
