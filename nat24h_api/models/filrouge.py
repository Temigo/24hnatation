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


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
    _type = VirtualField("TimeSlot")


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer




class TimeSlotSubscription(models.Model):
    class Meta:
        app_label = 'nat24h_api'
    user = models.ForeignKey(User)
    slot = models.ForeignKey(TimeSlot)
    # result = models.FloatField()


class TimeSlotSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlotSubscription
    _type = VirtualField("TimeSlotSubscription")


class TimeSlotSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = TimeSlotSubscription.objects.all()
    serializer_class = TimeSlotSubscriptionSerializer
    filter_fields = {
        'slot': ['exact'],
        'user': ['exact']}
