import sys
import os
PROJECT = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', )))

print ''
print 'NOTE:'
print 'Please ensure you do: export DJANGO_SETTINGS_MODULE="%s.settings" or similar as appropriate.' % PROJECT
print ''

sys.exit(1)
