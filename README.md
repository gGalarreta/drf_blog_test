# drf_blog_test
comands:
    create project: $docker-compose run --rm blog django-admin.py startproject drf_basics .
    create app: $docker-compose run --rm blog python manage.py startapp blog
    build app : $docker-compose build
    run app : $docker-compose run up

    write models:
        $ docker-compose run --rm blog python manage.py makemigrations (generate migrations)
        $ docker-compose run --rm blog python manage.py migrate (code to psql)
settings:

DB SETTINGS

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'blog_api',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432
        }
    }

    "PostgreSQL does not auto-create databases on first connection. You must create a database before you can use it."

    $ docker ps
    $ docker exec -it 24bd32322645  psql -U postgres

    psql:/ CREATE DATABASE blog_api_db WITH OWNER postgres ENCODING 'utf-8';

    $docker-compose run --rm blog python manage.py migrate


