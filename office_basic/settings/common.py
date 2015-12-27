"""Common settings and globals."""

from os.path import abspath, basename, dirname, join, normpath
from sys import path

from configurations import Configuration

from .logger import LoggerSettingsMixin


class Settings(LoggerSettingsMixin, Configuration):
    # ######### PATH CONFIGURATION
    # Absolute filesystem path to the Django project directory:
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    # Absolute filesystem path to the top-level project folder:
    SITE_ROOT = dirname(DJANGO_ROOT)

    # Site name:
    SITE_NAME = basename(DJANGO_ROOT)

    ALLOWED_HOSTS = ['*']

    # Add our project to our pythonpath, this way we don't need to type our project
    # name in our dotted import paths:
    path.append(DJANGO_ROOT)
    # ######### END PATH CONFIGURATION

    # ######### DEBUG CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = False
    # ######### END DEBUG CONFIGURATION

    # ######### MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = [
        ('Kush Jain', 'kushj.dev@gmail.com'),
    ]
    # ######### END MANAGER CONFIGURATION

    # ######### GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'UTC'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = False

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = False

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = False  # Default is False, but, purposefully made False to track it
    # ######### END GENERAL CONFIGURATION

    # ######### MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # ######### END MEDIA CONFIGURATION

    # ######### STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = [
        normpath(join(DJANGO_ROOT, 'assets')),
    ]

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]
    # ######### END STATIC FILE CONFIGURATION

    # ######### SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = r"(^bpa1ytu5$lpjc%3rnd2bbo9xhk-z(dse!e1^m*4lmo5_%&el"
    # ######### END SECRET CONFIGURATION

    # ######### FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = [
        normpath(join(DJANGO_ROOT, 'fixtures')),
    ]
    # ######### END FIXTURE CONFIGURATION

    # ######### TEMPLATE CONFIGURATION
    # https://docs.djangoproject.com/en/1.9/ref/templates/upgrading/
    # https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-TEMPLATES
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                normpath(join(DJANGO_ROOT, 'templates'))
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.core.context_processors.debug',
                    'django.core.context_processors.i18n',
                    'django.core.context_processors.media',
                    'django.core.context_processors.static',
                    'django.core.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                    'django.core.context_processors.request',
                ],
                'debug': property(lambda self: self.DEBUG)
            }
        }
    ]

    # ######### END TEMPLATE CONFIGURATION

    # ######### MIDDLEWARE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
    MIDDLEWARE_CLASSES = [
        # Default Django middleware.
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
    # ######### END MIDDLEWARE CONFIGURATION

    # ######### URL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
    ROOT_URLCONF = '{0}.urls'.format(SITE_NAME)
    # ######### END URL CONFIGURATION

    # ######### APP CONFIGURATION
    DJANGO_APPS = [
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        'django.contrib.humanize',

        # Admin panel and documentation:
        'django.contrib.admin',
        'django.contrib.admindocs'
    ]

    THIRD_PARTY_APPS = [
    ]

    LOCAL_APPS = [
        'elements.base',
        'elements.commute',
    ]

    # ######### END APP CONFIGURATION

    AUTH_USER_MODEL = 'base.User'

    # ######### EMAIL CONFIGURATION

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_HOST = ''
    EMAIL_PORT = 25
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''

    DEFAULT_FROM_EMAIL = 'kushj.dev@gmail.com'
    # ######### END EMAIL CONFIGURATION

    # ######### SESSION
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
    # ######### END SESSION

    # ######### WSGI CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'
    # ######### END WSGI CONFIGURATION

    # ######### COMPRESSION CONFIGURATION
    RESOURCE_VERSION = 1

    # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
    COMPRESS_ENABLED = True

    COMPRESS_OFFLINE = False

    # # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
    COMPRESS_CSS_FILTERS = [
        # 'compressor.filters.template.TemplateFilter',
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter'
    ]

    # # See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
    # COMPRESS_JS_FILTERS = [
    # 'compressor.filters.template.TemplateFilter',
    # ]

    COMPRESS_OUTPUT_DIR = 'compressed'

    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
    )
    COMPRESS_OFFLINE_IGNORE_FILES = (
        '.*site-packages.*',  # ignore all external apps templates
    )
    COMPRESS_OFFLINE_MANIFEST = 'manifest_{0}.json'.format(RESOURCE_VERSION)
    # ######### END COMPRESSION CONFIGURATION

    # ######### MISC
    # Robots.txt
    ALLOW_SEARCH_ENGINE_INDEXING = True
    # ######### END MISC

    # ######### PERIODIC TASKS

    # ######### END PERIODIC TASKS

    # ######### DEPENDANT SETTINGS -

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = property(lambda self: self.DJANGO_APPS + self.THIRD_PARTY_APPS + self.LOCAL_APPS)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = property(lambda self: self.ADMINS)
    SIGNUP_MAILING_LIST = property(lambda self: self.ADMINS)

    COMPRESS_URL = property(lambda self: self.STATIC_URL)
    COMPRESS_ROOT = property(lambda self: self.STATIC_ROOT)

    THUMBNAIL_DEFAULT_STORAGE = property(lambda self: self.DEFAULT_FILE_STORAGE)
    COMPRESS_STORAGE = property(lambda self: self.STATICFILES_STORAGE)

    # ######## END DEPENDANT SETTINGS

    # Test Settings
    TESTING = False
