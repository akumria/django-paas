import os

try:
    os.environ['DJANGO_SETTINGS_MODULE']
    from base import *
except KeyError:
    from notconfigured import *
