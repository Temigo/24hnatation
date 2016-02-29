"""
Django settings for nat24h project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')$w@s+3e_&cl19@c2-qbi^rr6fnzj4p*0%3u_xtltj0*-cc0&v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'corsheaders',
    'permission',
    'nat24h_base',
    'nat24h_activity',
    'import_export',
)


MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nat24h.urls'

WSGI_APPLICATION = 'nat24h.wsgi.application'

ATOMIC_REQUESTS = True

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/assets/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'assets/static/')

# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoObjectPermissions',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    )
}

# Auth

AUTHENTICATION_BACKENDS = (
    'nat24h.utils.AuthenticationBackend',
    # 'django.contrib.auth.backends.ModelBackend',
    'permission.backends.PermissionBackend',
)

AUTH_USER_MODEL = 'nat24h_base.User'

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=7 * 24),
}

# Permissions

PERMISSION_CHECK_PERMISSION_PRESENCE = True
PERMISSION_CHECK_TEMPLATES_OPTIONS_BUILTINS = False # ?? error while syncdb
PERMISSION_DEFAULT_APL_ANY_PERMISSION = False
PERMISSION_DEFAULT_APL_CHANGE_PERMISSION = True
PERMISSION_DEFAULT_APL_DELETE_PERMISSION = False

# CORS headers

CORS_ORIGIN_ALLOW_ALL = True
