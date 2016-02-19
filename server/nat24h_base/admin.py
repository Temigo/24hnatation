from django.contrib.auth import models
from django.contrib import admin

from nat24h_base.models import User, Profile, Group

#admin.site.register(models.Permission)


admin.site.register(User)
#admin.site.unregister(Group)
#admin.site.register(models.Group)
admin.site.register(Profile)


from nat24h.utils import get_permission
#for user in User.objects.all():
#    user.user_permissions.add(get_permission('nat24h_activity', 'add_activitysubscription'))
"""from django.contrib.auth.models import Group
Group.objects.get(name='default').permissions.add(get_permission('nat24h_activity', 'add_activitysubscription'))
Group.objects.get(name='default').save()"""
