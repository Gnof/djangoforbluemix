#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MODULE.settings")
    # Read port selected by the cloud for our application
    # VCAP_APP_PORT is also PORT in Bluemix Public
    PORT = '0.0.0.0:' + os.getenv('VCAP_APP_PORT', '8000')
    cmd = sys.argv

    for c in cmd:
        if c == 'runserver':
            if not PORT in cmd:
                cmd.append(PORT)

    from django.core.management import execute_from_command_line

    execute_from_command_line(cmd)
