from django.db import models
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from nat24h_api.models import VirtualField


class Activity(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    name = models.CharField(max_length=100)
    activity = models.ForeignKey(Activity)
    admin = models.ForeignKey(User)
    members = models.ManyToManyField(User)
    # result = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name + " (" + self.activity + ")" + unicode([self.admin] + self.members)
