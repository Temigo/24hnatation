from .dev_local import *

DEBUG = False

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'HOST': 'mysqldb',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

EMAIL_HOST = "frankiz"
EMAIL_PORT = 25

SESSION_COOKIE_SECURE = True
ALLOWED_HOSTS = ["*"]

DEFAULT_FROM_EMAIL = "24hnatation@binets.polytechnique.fr"
SERVER_EMAIL = "24hnatation@binets.polytechnique.fr" # redirige sur info@faerix.polytechnique.org
ADMINS = [("Webmaster 24hNatation", "laura.domine@polytechnique.edu")]
