from .common import *

DEBUG = True

TEMPLATE_DEBUG = True


INSTALLED_APPS = INSTALLED_APPS + (
    'django.contrib.staticfiles',
    'django_extensions',
    # 'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'django',
        # 'HOST': '127.0.0.1',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'PORT': 3306
    }
}
