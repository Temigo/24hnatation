from django.db import models
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from nat24h_api.models import VirtualField


class Activity(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=[
        ("individual", "individual"),
        ("team", "team"),
    ])

    def __unicode__(self):
        return self.name + " (" + self.type + ")"



class ActivityInscription(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    name = models.CharField(max_length=100)
    size_limit = models.IntegerField(default=None)
    activity = models.ForeignKey(Activity)
    members = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name + " (" + self.activity + ") [" + self.members + "]"
