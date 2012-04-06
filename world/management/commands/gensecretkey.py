from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand
from django.utils.crypto import get_random_string

import os

class Command(TemplateCommand):
    help = ("Generate a secret key. Optionally for a given project")

    def handle(self, project_name=None, *args, **options):
        if project_name is None:
            project_name = "paas"

        # check if the file exists, if so bailout
        secret_file = os.path.join(project_name, 'settings', 'secret.py')
        try:
            open(secret_file, "r")
        except IOError:
            pass
        else:
            raise CommandError("%s already exists." % secret_file)

        # check that the path exists, if not create it
        secret_dir = os.path.dirname(secret_file)
        if not os.path.exists(secret_dir):
            os.makedirs(secret_dir)

        # Create a random SECRET_KEY hash to put it in the main settings.
        # exactly from django.core.management.commands.startproject
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = get_random_string(50, chars)

        # write out the file
        secrets = open(secret_file, "w+")
        secret_line = "SECRET_KEY = '%s'\n" % secret_key
        secrets.write(secret_line)
        secrets.close()
