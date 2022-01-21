# FASTOR


## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
```

## install requirements

```bash
pip install -r requirements.txt
```

## Need to expose values for the following environment variables.
```commandline
SERVER_BASE_URL
POSTGRE_SQL_DB_NAME
POSTGRE_SQL_USER_NAME
POSTGRE_SQL_PASSWORD
```
## running django management commands & usage

```sh
export DJANGO_SETTINGS_MODULE=fastor.settings
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```