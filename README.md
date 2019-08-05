# HMS - Hours Manager System

This project is to demonstrate how to use TDD with Python.

## Modules

### [1. Companies](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/company 'Go to company path')

Module to define a company with your informations.

#### 1.1 Actions

* List all companies;
* Added new company;
* Remove one pointsheet;

#### 1.2 Fields

* _Name_ - Company's name.
* _Description_ - Lettle description about company, specification or comments.
* _Active_ - Status to be active (`True`) or deactive (`False`).
* _Date create_ - Date time when this row was created.
* _Date update_ - Date time when this row was updated.

### [2. Pointsheets](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/pointsheets 'Go to Pointsheets path')

Module to define monthly the pointsheets's informations for one Company.

#### 2.1 Actions

* List all pointsheets;
* Added new pointsheet;
* Update a pointsheet;
* Remove one pointsheet;

#### 2.2 Fields

* _Year_ - Year when the pointsheet was registred.
* _Month_ - Month when the pointsheet was registred.
* _Active_ - Status to be active (`True`) or deactive (`False`).
* _Date create_ - Date time when this row was created.
* _Date update_ - Date time when this row was updated.
* _Company_ - Company that it's related.

### [3. Launches](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/launches 'Go to launches path')

Module to define daily launches's informations to pointsheets.

#### 3.1 Actions

* List all launches;
* Added new launch;
* Active/deactivate a launch;

#### 3.2 Fields

* _Date_ - Date when the launch was registred.
* _Time_ - Time (hour and minute) when the launch was registred.
* _Active_ - Status to be active (`True`) or deactive (`False`).
* _Date create_ - Date time when this row was created.
* _Date update_ - Date time when this row was updated.
* _Pointsheet_ - Pointsheet that it's related.

### [4. Dashboard](https://github.com/fbrump/hours-management-system/tree/master/hoursManagementSystem/dashboard 'Go to dashboard path')

_Building.._

## Envionmnet

Setting venv system:

    pip install -r requirements.txt --no-index --find-links file:///tmp/packages

Migrate data base for startup:

    python hoursManagementSystem/manage.py makemigrations
    python hoursManagementSystem/manage.py migrate

Run server:

    python hoursManagementSystem/manage.py runserver

### Setup

* Python
* Django
* Django-bulma
* Django.test
* SQLite3
