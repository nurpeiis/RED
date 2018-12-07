from RED.settings.base import *
import os
#Overwrite base settings here
# Read secret key from a file
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
server {
    listen 80 default_server;
    return 444;
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
try:
    from RED.settings.base import *
except:
    pass