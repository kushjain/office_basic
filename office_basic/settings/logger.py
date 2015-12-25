# Logger Configurations
from os.path import dirname, abspath, join, exists
import os


class LoggerSettingsMixin(object):

    # Create a local log directory if log_file does not exist.
    root = dirname(dirname(dirname(abspath(__file__))))
    log_dir = join(root, 'log')
    if not exists(log_dir):
        os.makedirs(log_dir)
    file_name = join(log_dir, 'element.log')

    LOG_FILE = os.environ.get('LOG_FILE', file_name)

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(asctime)s [%(levelname)s] logger=%(name)s '
                          'process=%(process)d thread=%(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            }
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler',
            },
            'file_handler': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',   # can set up RotatingFileHandler also. Specify maxBytes, backupCount
                'filename': LOG_FILE,
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            'apps': {
                'handlers': ['console', 'file_handler'],
                'level': 'DEBUG',
                'propagate': False,
            },

            # Catch All Logger -- Captures any other logging
            '': {
                'handlers': ['console', 'file_handler'],
                'level': 'INFO',
                'propagate': True,
            }
        }
    }
