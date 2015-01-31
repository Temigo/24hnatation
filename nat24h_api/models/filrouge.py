from django.db import models
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from nat24h_api.models import VirtualField


class TimeSlot(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    start = models.DateTimeField()
    end = models.DateTimeField()
    value = models.FloatField()

    def __unicode__(self):
        return "slot %s : %s" % (self.start, self.end)


class TimeSlotSubscription(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    user = models.ForeignKey(User)
    # result = models.FloatField()
