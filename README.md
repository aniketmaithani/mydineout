# mydineout

[![Build Status](https://travis-ci.com/aniketmaithani/mydineout.svg?token=oSFWgtSbfV6Xh4RcbPpE&branch=master)](https://travis-ci.com/aniketmaithani/mydineout)


[![codecov](https://codecov.io/gh/aniketmaithani/mydineout/branch/master/graph/badge.svg)](https://codecov.io/gh/aniketmaithani/mydineout)


## Getting started
- Before starting make sure you have `git` installed on your system.
- The project uses postgres and gdal libraries. In order to install them on your system follow the instructions [here.](https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/)
- Once you have setup `postgres` make sure you create an extension in your database such as `psql -d <database_name> -c "CREATE EXTENSION postgis;`
- The following project uses PSQL >= 11
- To get more insight about the project and development refer to the project wiki [here](https://github.com/aniketmaithani/mydineout/wiki)

## Running the application 
- Clone the repo on your system
- For e.g sake we are using `postgres` as the database but you can configure other db's also
- Once you've cloned the repo, activate your `virtualenv`
- Install `pip install -r requirements/development.txt` file while you are in dev mode
- Take a look at the `.env.sample` file and fill the values as per your requirement.
- Once the setup is completed, run migration `python manage.py migrate`.
- Once this is done create superuser : `python manage.py createsuperuser`
- Run the app : `python manage.py runserver` 


### FOR PRODUCTION : In case you want to use this app in production make sure you have prod related dependencies installed and your keys and secrets are in an `.env` file. 

# * ANYTHING IN MASTER IS ALWAYS DEPLOYABLE * 
