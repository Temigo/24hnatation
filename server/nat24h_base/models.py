#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, _user_has_module_perms, _user_has_perm
from rest_framework import viewsets, serializers, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from nat24h.utils import get_default_permission_group
from nat24h.utils import VirtualField


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'password', 'user_permissions')
        read_only_fields = ('last_login', 'date_joined', 'is_superuser', 'is_staff')
    _type = VirtualField("User")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = {
        'email': ['exact']}


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        unserializer = UserSerializer(data=request.data)
        unserializer.is_valid(raise_exception=True)
        user = unserializer.save()
        # if 'password' in request.data:
        #     user.set_password(request.data['password'])
        user.set_password('password')
        user.groups.add(get_default_permission_group())
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, 201)


class Group(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=[
        ("school", "École"),
        ("binet", "Asso/Binet"),
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
    groups = models.ManyToManyField(Group, blank=True)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
    _type = VirtualField("Profile")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_fields = {
        'user': ['exact']}


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(get_default_permission_group())
        instance.save()
        Profile.objects.create(user=instance)
