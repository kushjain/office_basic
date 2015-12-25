"""Development settings and globals."""
from . import common


class Settings(common.Settings):
    """
    Common Development Settings
    """

    DEVELOPMENT_ENV = True

    # ######### DEBUG CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = True

    # ######### DATABASE CONFIGURATION

    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',        # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
    # ######### END DATABASE CONFIGURATION


    # ########## EMAIL CONFIGURATION
    # # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # ########## END EMAIL CONFIGURATION

    # ######### CACHE CONFIGURATION
    # ######### END CACHE CONFIGURATION

    COMPRESS_OFFLINE = True
