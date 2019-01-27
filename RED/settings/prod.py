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
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)

DEFAULT_FROM_EMAIL = 'NYUAD Office of Community & Education Engagement- CoLab <noreply@nyuadengage.com>'
EMAIL_SUBJECT_PREFIX = '[RED] '
#avoid transmitting the CSRF & sessing cookie over HTTP accidentaly
CSRF_COOKIE_SECURE= True
SESSION_COOKIE_SECURE = True
#Performance optimization

try:
    from RED.settings.base import *
except:
    pass