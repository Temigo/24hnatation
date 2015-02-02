# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('nat24h_api', '0002_auto_20150202_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='admin',
            field=models.ForeignKey(related_name='owned_team_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
