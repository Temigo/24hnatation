from rest_framework import fields

class VirtualField(fields.ReadOnlyField):
    type_name = 'VirtualField'
    type_label = 'virtual'
    label = 'virtual'
    source = ''

    def __init__(self, value):
        super(VirtualField, self).__init__()
        self.value = value

    def get_attribute(self, instance):
        return ''

    def to_representation(self, attr):
        return self.value


from django.contrib.auth.models import Permission

def get_permission(app, name):
    return Permission.objects.get(codename=name, content_type__app_label=app)


from django.contrib.auth.models import Group

def get_default_permission_group():
    """try:
        return Group.objects.get(name='default')
    except Group.DoesNotExist:"""
    g = Group.objects.create(name='default')
    g.permissions.add(get_permission('nat24h_base', 'add_group'))
    g.permissions.add(get_permission('nat24h_activity', 'add_team'))
    g.permissions.add(get_permission('nat24h_activity', 'add_teamsubscription'))
    g.permissions.add(get_permission('nat24h_activity', 'add_timeslotsubscription'))
    g.permissions.add(get_permission('nat24h_activity', 'add_activitysubscription'))
    g.save()
    return g


from django.contrib.auth.backends import ModelBackend

class AuthenticationBackend(ModelBackend):
    def has_perm(self, user_obj, perm, obj=None):

        #user_obj.groups.add(get_default_permission_group())
        #user_obj.save()
        #print get_default_permission_group().permissions
        """if 'nat24h_activity.add_timeslotsubscription' in user_obj.get_all_permissions():
            if 'nat24h_activity.add_activitysubscription' not in user_obj.get_all_permissions():
                user_obj.user_permissions.add(get_permission('nat24h_activity', 'add_activitysubscription'))
"""
        print user_obj, perm, obj
        print user_obj.get_all_permissions()
        return super(AuthenticationBackend, self).has_perm(user_obj, perm, obj)
