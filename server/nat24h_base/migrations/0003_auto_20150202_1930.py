# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nat24h_base', '0002_auto_20150202_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='type',
            field=models.CharField(max_length=25, choices=[(b'school', b'\xc3\x89cole'), (b'binet', b'Asso/Binet'), (b'section', b'Section')]),
            preserve_default=True,
        ),
    ]
