from permission.logics import AuthorPermissionLogic

PERMISSION_LOGICS = (
    ('nat24h_base.Profile', AuthorPermissionLogic(field_name='user')),
)
