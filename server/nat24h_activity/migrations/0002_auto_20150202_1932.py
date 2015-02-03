# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nat24h_activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 19, 32, 5, 982258, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 19, 32, 8, 863161, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
