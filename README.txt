
change
	mv paas to <myproject>

	OPTIONAL:
	So long as the environment variable 'DJANGO_SETTINGS_MODULE' is set, not required.

	edit manage.py
		- DJANGO_SETTINGS_MODULE and change 'paas' to <myproject>

	create <myproject>/settings/secret.py:
		SECRET_KEY = ''
	Some long value
