# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20150427_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stool',
            name='day_of_life',
        ),
    ]
