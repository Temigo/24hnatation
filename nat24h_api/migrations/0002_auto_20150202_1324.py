# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nat24h_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('activity', models.ForeignKey(to='nat24h_api.Activity')),
                ('admin', models.ForeignKey(related_name='owned_team', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='activityinscription',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='activityinscription',
            name='members',
        ),
        migrations.DeleteModel(
            name='ActivityInscription',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='type',
        ),
    ]
