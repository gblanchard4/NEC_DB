# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0020_auto_20150512_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='uvva',
            field=models.CharField(max_length=2, verbose_name=b'UV/VA', choices=[(b'N', b'None'), (b'UA', b'UA'), (b'UV', b'UV')]),
        ),
    ]
