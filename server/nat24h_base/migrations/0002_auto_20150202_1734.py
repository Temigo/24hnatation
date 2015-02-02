# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nat24h_base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
