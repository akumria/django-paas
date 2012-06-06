Django PaaS - Django on Platform as a Service (PaaS) providers
==============================================================

This is a minimal Django project to allow you to easily get setup on
various PaaS providers.

Currently there is support for:

* Heroku

Initial (local) install.
------------------------

- clone this project

        $ git clone https://github.com/akumria/django-paas
        $ cd django-paas

- setup your virtual environment (one time)

        $ virtualenv --no-site-packages env
        $ virtualenv --relocatable env
        $ source env/bin/activate

- install dependancies

        (env)$ pip install -r requirements.txt

- generate a secret key and save it

        (env)$ ./manage.py gensecretkey

    - this will output 'Please create secret.py and specify a SECRET_KEY within.' but this is OK

        (env)$ git add pass/settings/secret.py
        (env)$ git commit -m "Generated secret key"

- rename the project

        (env)$ git mv paas to <myproject>

	- edit manage.py

         - change 'paas.settings' to '<myproject>.settings'

        (env)$ git add manage.py

	- edit <myproject>/settings/base.py

		- specify appropriate value for ADMINS=

        (env)$ git add .
        (env)$ git commit -m "Updated to name to be <myproject>"

You will now have a local installation, using sqllite where you can add 
additional applications and test things locally.

- run things!

        (env)$ ./manage.py syncdb
        (env)$ ./manage.py migrate
        (env)$ ./manage.py runserver

Deploying to Heroku
-------------------

1. If you have not already, please sign up. (one off)

	- visit https://api.heroku.com/signup
	- enter your email address
	- check you email and confirm your account

2. Install the Heroku toolbelt.

	- visit https://toolbelt.heroku.com/
	- follow the instructions to install on screen

3. Login

        (env)$ heroku login

4. Create the remote Heroku stack

        (env)$ heroku create --stack cedar
	- Note down the URL generated, this is where your app will live (for now)

5. Upload the code remotely

        (env)$ git push heroku master
	- Note this will take a while

6. Export the Django settings (locally and remotely)

        (env)$ export DJANGO_SETTINGS_MODULE=paas.settings.heroku
    - change to <myproject> if you have renamed as above

        (env)$ heroku config:add DJANGO_SETTINGS_MODULE=paas.settings.heroku
    - likewise change to <myproject>

7. Add a remote Heroku database and perform setup

        (env)$ heroku addons:add heroku-postgresql:dev
	- Note the line 'Attached as HEROKU_POSTGRESQL_FOO'  # note it is unlikely to be FOO

        (env)$ heroku pg:promote HEROKU_POSTGRESQL_FOO
        (env)$ heroku run python manage.py syncdb
        (env)$ heroku run python manage.py migrate

8. Visit your site

        (env)$ heroku open

Deploying to a generic PaaS
---------------------------

	- create a deployment environment file (e.g. paas/settings/generic.py)
		- specify your DB
		- specify your environment ADMINS=
