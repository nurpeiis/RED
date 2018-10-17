from RED.settings.base import *

#Overwrite base settings here
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from RED.settings.base import *
except:
    pass