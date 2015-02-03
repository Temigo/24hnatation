# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nat24h_base', '0003_auto_20150202_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(to='nat24h_base.Group', blank=True),
            preserve_default=True,
        ),
    ]
