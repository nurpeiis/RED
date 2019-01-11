from RED.settings.base import *
from decouple import config, Csv
import dj_database_url
#Overwrite base settings here
# Read secret key from a file
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=60
    )
}

#For email sending use SendGrid: use this tutorial https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html
EMAIL_HOST      = 'my-domain.com'
EMAIL_HOST_PASSWORD = 'my cpanel password'
EMAIL_HOST_USER = 'my cpanel user'
EMAIL_PORT      = 25
EMAIL_USE_TLS   = False
DEFAULT_FROM_EMAIL  = 'webmaster@my-host.com'
SERVER_EMAIL    = 'root@my-domain.com'

#avoid transmitting the CSRF & sessing cookie over HTTP accidentaly
CSRF_COOKIE_SECURE= True
SESSION_COOKIE_SECURE = True
#Performance optimization

try:
    from RED.settings.base import *
except:
    pass