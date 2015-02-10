# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nat24h_base', '0004_auto_20150203_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.CharField(unique=True, max_length=128)),
                ('full_name', models.CharField(max_length=128, blank=True)),
                ('pseudo', models.CharField(max_length=128, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
