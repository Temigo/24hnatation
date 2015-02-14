from .dev_local import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'HOST': 'mysqldb',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

EMAIL_HOST = "frankiz"
EMAIL_PORT = 25
