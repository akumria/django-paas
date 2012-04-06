Django PaaS - Django on Platform as a Service (PaaS) providers

This is a minimal Django project to allow you to easily get setup on
various PaaS providers.

Currently there is support for:
	- None

Initial (local) install.
	- clone this project
	- setup your virtual environment
	- run ./manage.py gensecretkey
		- this will output 'Please create secret.py and specify a SECRET_KEY within.' but this is OK
	- git mv paas to <myproject>
	- edit manage.py
		- change 'paas.settings' to '<myproject>.settings'
	- edit <myproject>/settings/base.py
		- specify appropriate value for ADMINS=

You will now have a local installation, using sqllite where you can add 
additional applications and test things locally.

	- run things!
		- ./manage.py syncdb
		- ./manage.py migrate
		- ./manage.py runserver

Deploying to a PaaS 
	- create a deployment environment file (e.g. paas/settings/staging.py)
		- specify your DB
		- specify your environment ADMINS=
