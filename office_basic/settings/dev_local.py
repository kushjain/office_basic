from . import dev


class Settings(dev.Settings):

    # ######### DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'element',        # Or path to database file if using sqlite3.
            'USER': 'admin',                      # Not used with sqlite3.
            'PASSWORD': 'kush@201599',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

    # ########## END DATABASE CONFIGURATION
