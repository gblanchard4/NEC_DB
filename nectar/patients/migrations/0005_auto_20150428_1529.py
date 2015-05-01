# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_remove_stool_day_of_life'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='sequence_file',
            field=models.CharField(max_length=30, verbose_name=b'Sequece File Name'),
        ),
    ]
