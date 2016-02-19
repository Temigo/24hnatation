from .common import *

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
