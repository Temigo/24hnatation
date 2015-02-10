from django.db import models
from rest_framework import viewsets, serializers
from nat24h_base.models import User
from nat24h.utils import VirtualField


class Activity(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.name


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
    _type = VirtualField("Activity")


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer



class Team(models.Model):
    name = models.CharField(max_length=100)
    activity = models.ForeignKey(Activity)
    admin = models.ForeignKey(User, related_name="owned_team_set")
    # result = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name + " (activity: " + unicode(self.activity) + ", admin: " + unicode(self.admin) + ")"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
    _type = VirtualField("Team")


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ['activity']



class TeamSubscription(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    # result = models.FloatField()

    def __unicode__(self):
        return "%s : %s" % (unicode(self.team), unicode(self.user))


class TeamSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSubscription
    _type = VirtualField("TeamSubscription")

    def create(self, data):
        request = self.context['request']
        data['user'] = request.user
        return super(TeamSubscriptionSerializer, self).create(data)


class TeamSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = TeamSubscription.objects.all()
    serializer_class = TeamSubscriptionSerializer
    filter_fields = {
        'team': ['exact'],
        'user': ['exact']}




class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    value = models.FloatField()

    def __unicode__(self):
        return "slot %s - %s (value: %d)" % (self.start.strftime('%H:%M'), self.end.strftime('%H:%M'), self.value)


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
    _type = VirtualField("TimeSlot")


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer



class TimeSlotSubscription(models.Model):
    user = models.ForeignKey(User)
    slot = models.ForeignKey(TimeSlot)
    # result = models.FloatField()

    def __unicode__(self):
        return "%s : %s" % (unicode(self.slot), unicode(self.user))


class TimeSlotSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlotSubscription
    _type = VirtualField("TimeSlotSubscription")

    def create(self, data):
        request = self.context['request']
        data['user'] = request.user
        return super(TimeSlotSubscriptionSerializer, self).create(data)


class TimeSlotSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = TimeSlotSubscription.objects.all()
    serializer_class = TimeSlotSubscriptionSerializer
    filter_fields = {
        'slot': ['exact'],
        'user': ['exact']}
