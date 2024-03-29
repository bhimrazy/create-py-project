# Vannila Python App

This is a python app starter repository.
Follow these commands to run the project.

## Setup

```shell
    #create a python environment
    $ python -m venv venv
    #activate environment
    $ source venv/bin/activate # use venv/Scripts/activate for windows
    #install packages from requirements.txt file
    $ pip install -r requirements.txt

    # Training
    $ python main.py --task train

    # Run app
    $ uvicorn app.api:app --reload # dev
    $ uvicorn app.api:app # prod

    # Run test and coverage
    $ pytest
    $ coverage run -m pytest
    $ coverage report -i

    # Run flake8
    $ flake8

```
