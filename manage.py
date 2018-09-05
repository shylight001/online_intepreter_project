#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    if 'RDS_DB_NAME' in os.environ: # online setting file
        setting_file = 'online_intepreter_project.settings.dev'
    else:
        setting_file = 'online_intepreter_project.settings.local'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting_file)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
