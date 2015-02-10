from django.contrib.auth import models
from django.contrib import admin

from nat24h_base.models import User, Profile, Group

admin.site.register(User)
admin.site.unregister(models.Group)
admin.site.register(Profile)
admin.site.register(Group)
