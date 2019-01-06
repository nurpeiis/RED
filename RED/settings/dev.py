from RED.settings.base import *

#Overwrite base settings here
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'reddb',
        'USER': 'postgres',
        'PASSWORD': 'b.nurpeis5553141',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


try:
    from RED.settings.base import *
except:
    pass