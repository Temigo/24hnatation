#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import viewsets, serializers
from nat24h_api.models import VirtualField


class Group(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=[
        ("school", "École"),
        ("binet", "Binet"),
        ("section", "Section"),
    ])

    def __unicode__(self):
        return self.name + " (" + self.type + ")"
