#!/usr/bin/env python
import os
import sys

from office_basic.libs.utils import get_default_django_settings_module


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')
    # NOTE: Change DJANGO_SETTINGS_MODULE instead of DJANGO_CONFIGURATION class for each environment
    # Thus, we keep the same class (i.e. Settings) for all environments.
    #
    # So instead of having classes like 'Common', 'Prod', 'Dev' in the module 'office_basic.settings',
    # We would have class 'Settings' in modules 'office_basic.settings.common', 'office_basic.settings.production',
    # 'bluehornet.settings.dev', etc.

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
