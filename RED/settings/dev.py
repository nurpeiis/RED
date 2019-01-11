from RED.settings.base import *
from decouple import config, Csv
import dj_database_url
#Overwrite base settings here
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=60
    )
}

#For email debugging purposes
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

try:
    from RED.settings.base import *
except:
    pass