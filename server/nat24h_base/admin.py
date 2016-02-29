from django.contrib.auth import models
from django.contrib import admin

from nat24h_base.models import User, Profile, Group
from import_export import resources, fields
#admin.site.register(models.Permission)
from import_export.admin import ImportExportModelAdmin



class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    pass

class ProfileResource(resources.ModelResource):
    full_groups = fields.Field()

    class Meta:
        model = Profile
        fields = ('user__first_name', 'user__last_name', 'user__email')

    def dehydrate_full_groups(self, profile):
        groups = profile.groups.all()
        s = ""
        for g in groups:
            s = s + " | %s | " % g.name
        return s

class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    pass

admin.site.register(User, UserAdmin)
#admin.site.unregister(Group)
#admin.site.register(models.Group)
admin.site.register(Profile, ProfileAdmin)

from nat24h.utils import get_permission
#for user in User.objects.all():
#    user.user_permissions.add(get_permission('nat24h_activity', 'add_activitysubscription'))
"""from django.contrib.auth.models import Group
Group.objects.get(name='default').permissions.add(get_permission('nat24h_activity', 'add_activitysubscription'))
Group.objects.get(name='default').save()"""
"""u = User.objects.get(id=14)
print "Hi"
print u
u.set_password("f5r4lw")
u.save()"""
