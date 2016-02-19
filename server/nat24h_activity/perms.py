from permission.logics import AuthorPermissionLogic

PERMISSION_LOGICS = (
    ('nat24h_activity.ActivitySubscription', AuthorPermissionLogic(field_name='user', delete_permission=True)),
    ('nat24h_activity.TeamSubscription', AuthorPermissionLogic(field_name='user', delete_permission=True)),
    ('nat24h_activity.TeamSubscription', AuthorPermissionLogic(field_name='team__admin', delete_permission=True)),
    ('nat24h_activity.TimeSlotSubscription', AuthorPermissionLogic(field_name='user', delete_permission=True)),
    ('nat24h_activity.Team', AuthorPermissionLogic(field_name='admin', delete_permission=False)),
)
