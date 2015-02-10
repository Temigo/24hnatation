from permission.logics import AuthorPermissionLogic

PERMISSION_LOGICS = (
    ('nat24h_activity.TeamSubscription', AuthorPermissionLogic(field_name='user')),
    ('nat24h_activity.TimeSlotSubscription', AuthorPermissionLogic(field_name='user')),
    ('nat24h_activity.Team', AuthorPermissionLogic(field_name='admin')),
)
