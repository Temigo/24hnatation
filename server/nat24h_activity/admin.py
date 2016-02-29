from django.contrib import admin

from nat24h_activity.models import Activity, ActivitySubscription, Team, TeamSubscription, TimeSlot, TimeSlotSubscription

from import_export import resources, fields
#admin.site.register(models.Permission)
from import_export.admin import ImportExportModelAdmin



class TimeSlotSubscriptionResource(resources.ModelResource):
    class Meta:
        model = TimeSlotSubscription
        fields = ('user__first_name', 'user__last_name', 'slot__start', 'slot__end')

class TimeSlotSubscriptionAdmin(ImportExportModelAdmin):
    resource_class = TimeSlotSubscriptionResource
    pass

class ActivitySubscriptionResource(resources.ModelResource):
    class Meta:
        model = ActivitySubscription
        fields = ('user__first_name', 'user__last_name', 'activity__name')

class ActivitySubscriptionAdmin(ImportExportModelAdmin):
    resource_class = ActivitySubscriptionResource
    pass

class TeamSubscriptionResource(resources.ModelResource):
    class Meta:
        model = TeamSubscription
        fields = ('user__first_name', 'user__last_name', 'team__name')

class TeamSubscriptionAdmin(ImportExportModelAdmin):
    resource_class = TeamSubscriptionResource
    pass

admin.site.register(Activity)
admin.site.register(ActivitySubscription, ActivitySubscriptionAdmin)
admin.site.register(Team)
admin.site.register(TeamSubscription, TeamSubscriptionAdmin)
admin.site.register(TimeSlot)
admin.site.register(TimeSlotSubscription, TimeSlotSubscriptionAdmin)
