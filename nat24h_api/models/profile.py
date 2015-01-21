from django.db import models
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from nat24h_api.models import VirtualField
from nat24h_api.models.group import Group


class Profile(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    user = models.OneToOneField(User)
    groups = models.ManyToManyField(Group)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name + " " + self.surname
