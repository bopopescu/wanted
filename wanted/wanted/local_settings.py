import os
from . import settings


SECRET_KEY = '06zyl3erpfrz=myi%2@g7&e-%-wyl^-3b^flmg4yw2w_^7=^f^'


DATABASES = {
    # postgres on virtualbox
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wanted',
        'USER': 'admin',
        'PASSWORD': 'admin',
 #       'HOST': '192.168.7.59',
        'HOST' : '192.168.1.215' ,
        'PORT': '5432',

    },
    '_default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}