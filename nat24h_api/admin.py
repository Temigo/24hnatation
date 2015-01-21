from django.contrib import admin

from nat24h_api.models.activity import Activity
from nat24h_api.models.group import Group
from nat24h_api.models.profile import Profile

admin.site.register(Activity)
admin.site.register(Group)
admin.site.register(Profile)
