# HMS - Houres Manager System

This project is to demonstrate how to use TDD with Python.

## Modules

### 1. Companies

Module to define a company with your informations.

#### Actions

* List all companies;
* Added new company;
* Remove one pointsheet;

#### Fields

- name
    Company's name.
- description
    Lettle description about company, specification or comments.
- active
    Status to be active (`True`) or deactive (`False`).
- date create
    Date time when this row was created.
- date update
    Date time when this row was updated.

### 2. Pointsheets

Module to define monthly the pointsheets's informations for one [Company]( 'Company module').

#### Actions

* List all pointsheets;
* Added new pointsheet;
* Update a pointsheet;
* Remove one pointsheet;

#### Fields

- year
    Year when the pointsheet was registred.
- month
    Month when the pointsheet was registred.
- active
    Status to be active (`True`) or deactive (`False`).
- date create
    Date time when this row was created.
- date update
    Date time when this row was updated.
- company
    Company that it's relate.

### 3. Launches

Building..

### 4. Dashboard

_Building.._

## Envionmnet

Setting venv system:
    
    $ pip install -r requirements.txt --no-index --find-links file:///tmp/packages

Migrate data base for startup:
    
    python hoursManagementSystem/manage.py migrate

Run server:
    
    python hoursManagementSystem/manage.py runserver

### Setup

- Python
- Django
- Django-bulma
- Django.test
- SQLite3

