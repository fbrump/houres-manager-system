HMS - Houres Manager System
======

This project is to demonstrate how to use TDD with Python.

## Modules

### [1. Companies](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/company 'Go to company path')

Module to define a company with your informations.

#### Actions

* List all companies;
* Added new company;
* Remove one pointsheet;

#### Fields

- Name

    Company's name.

- Description

    Lettle description about company, specification or comments.
    
- Active

    Status to be active (`True`) or deactive (`False`).
    
- Date create

    Date time when this row was created.
    
- Date update

    Date time when this row was updated.

### [2. Pointsheets](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/pointsheets 'Go to Pointsheets path')

Module to define monthly the pointsheets's informations for one Company.

#### Actions

* List all pointsheets;
* Added new pointsheet;
* Update a pointsheet;
* Remove one pointsheet;

#### Fields

- Year

    Year when the pointsheet was registred.
    
- Month 

    Month when the pointsheet was registred.
    
- Active
    
    Status to be active (`True`) or deactive (`False`).
    
- Date create

    Date time when this row was created.
    
- Date update
    
    Date time when this row was updated.
    
- Company
    
    Company that it's relate.

### [3. Launches](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/launches 'Go to launches path')

Building..

### [4. Dashboard](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/dashboard 'Go to dashboard path')

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

