from django.contrib import admin

from nat24h_activity.models import Activity, Team, TimeSlot, TimeSlotSubscription

admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(TimeSlot)
admin.site.register(TimeSlotSubscription)
