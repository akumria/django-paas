Django PaaS - Django on Platform as a Service (PaaS) providers

This is a minimal Django project to allow you to easily get setup on
various PaaS providers.

Currently there is support for:
	- None

Initial (local) install.
	- clone this project
		- $ git clone https://github.com/akumria/django-paas
		- $ cd django-paas

	- setup your virtual environment (one time)
		- $ virtualenv --no-site-packages env
		- $ virtualenv --relocatable env
		- $ source env/bin/activate

	- install dependancies
		- (env)$ pip install -r requirements.txt

	- generate a secret key and save it
		- (env)$ ./manage.py gensecretkey
		- this will output 'Please create secret.py and specify a SECRET_KEY within.' but this is OK
		- (env)$ git add pass/settings/secret.py
		- (env)$ git commit -m "Generated secret key"

	- rename the project
		- (env)$ git mv paas to <myproject>

		- edit manage.py
			- change 'paas.settings' to '<myproject>.settings'
			- (env)$ git add manage.py

		- edit <myproject>/settings/base.py
			- specify appropriate value for ADMINS=
			- (env)$ git add .

		- (env)$ git commit -m "Updated to name to be <myproject>"

You will now have a local installation, using sqllite where you can add 
additional applications and test things locally.

	- run things!
		- (env)$ ./manage.py syncdb
		- (env)$ ./manage.py migrate
		- (env)$ ./manage.py runserver

Deploying to a PaaS 
	- create a deployment environment file (e.g. paas/settings/staging.py)
		- specify your DB
		- specify your environment ADMINS=
