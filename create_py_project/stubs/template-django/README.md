# Django Starter App

This is a django starter project repository.
Follow these commands to run the project.

## Setup

```shell
    #create a python environment
    $ python -m venv venv
    #activate environment
    $ source venv/bin/activate # use venv/Scripts/activate for windows
    #install packages from requirements.txt file
    $ pip install -r requirements.txt
    #migrate
    $ python manage.py migrate

    # Run app
    $ python manage.py runserver # dev
    $ gunicorn core.wsgi # prod

    # Run test and coverage
    $ python manage.py test
    $ coverage run manage.py test
    $ coverage report -i

    # Run flake8
    $ flake8

```
