# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20150511_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stool',
            name='feeds',
            field=models.CharField(max_length=1, verbose_name=b'Feeding', choices=[(b'F', b'Formula'), (b'B', b'Breast Milk'), (b'N', b'NPO'), (b'M', b'Mixed')]),
        ),
    ]
