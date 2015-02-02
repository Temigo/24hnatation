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



class Profile(models.Model):
    user = models.OneToOneField(User)
    groups = models.ManyToManyField(Group)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name + " " + self.surname


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
    _type = VirtualField("Profile")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_fields = {
        'user': ['exact']}
