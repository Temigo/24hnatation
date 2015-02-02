#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from nat24h.utils import VirtualField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    _type = VirtualField("User")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class Group(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=[
        ("school", "École"),
        ("binet", "Binet"),
        ("section", "Section"),
    ])
    members = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name + " (" + self.type + ")"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
    _type = VirtualField("Group")


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_fields = {
        'type': ['exact']}
    search_fields = ('name')
