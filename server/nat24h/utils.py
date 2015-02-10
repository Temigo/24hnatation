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
    try:
        return Group.objects.get(name='default')
    except Group.DoesNotExist:
        g = Group.objects.create(name='default')
        g.permissions.add(get_permission('nat24h_base', 'add_group'))
        g.permissions.add(get_permission('nat24h_activity', 'add_team'))
        g.permissions.add(get_permission('nat24h_activity', 'add_teamsubscription'))
        g.permissions.add(get_permission('nat24h_activity', 'add_timeslotsubscription'))
        g.save()
        return g
