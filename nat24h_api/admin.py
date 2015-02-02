from django.contrib import admin

from nat24h_api.models.profile import User, Profile, Group
from nat24h_api.models.activity import Activity, Team
from nat24h_api.models.filrouge import TimeSlot, TimeSlotSubscription


# admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(TimeSlot)
admin.site.register(TimeSlotSubscription)
