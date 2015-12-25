import os

from . import common


class Settings(common.Settings):
    # DEBUG CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = os.environ['DEBUG'].lower() == "true"

    # DATABASE CONFIGURATION
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
    # END DATABASE CONFIGURATION

    # Admin Accounts
    ADMIN_USER_ACCOUNTS = [
        {
            "email": 'kushj@gmail.com',
            "username": "element",
            "password": "pbkdf2_sha256$24000$elGnBF18MCk9$+jsfiE8wNLG6ME7Cb7fZP3ByK8wDIsTe1Ff0EDF+lbo=",
            "force_update_password": True
        }
    ]
    
    THIRD_PARTY_APPS = common.Settings.THIRD_PARTY_APPS + [
        'storages',
    ]

    # COMPRESSION CONFIGURATION
    COMPRESS_OFFLINE = True
    # END COMPRESSION CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = property(lambda self: 'https://{0}.s3.amazonaws.com/'.format(self.AWS_STATIC_STORAGE_BUCKET_NAME))

    MEDIA_URL = property(lambda self: 'https://{0}.s3.amazonaws.com/'.format(self.AWS_STORAGE_BUCKET_NAME))
