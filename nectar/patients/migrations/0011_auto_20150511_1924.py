# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_auto_20150511_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='rom',
            field=models.IntegerField(verbose_name=b'ROM in Hours'),
        ),
    ]
