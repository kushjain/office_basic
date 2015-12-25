import imp


def get_default_django_settings_module():
    try:
        file_ = imp.find_module('dev_local', ['office_basic/settings'])[0]
    except ImportError:
        default_django_settings_module = "office_basic.settings.dev"
    else:
        default_django_settings_module = "office_basic.settings.dev_local"
        file_.close()
    return default_django_settings_module
