from .base import *

import urlparse

# overrides so that things work correctly with Heroku
# grabbed from https://github.com/jacobian/django-dev-dashboard/commit/2bcf2890687b546cfb5625ff2874d9a20abca093

# Make sure urlparse understands custom config schemes.
urlparse.uses_netloc.append('postgres')

# Grab database info
db_url = urlparse.urlparse(os.environ['DATABASE_URL'])
DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql_psycopg2',
        'NAME':     db_url.path[1:],
        'USER':     db_url.username,
        'PASSWORD': db_url.password,
        'HOST':     db_url.hostname,
        'PORT':     db_url.port,
    }
}
