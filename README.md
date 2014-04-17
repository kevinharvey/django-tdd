django-tdd
==========

A Django management command to run tests every time a file is saved.

Installation
===

    pip install django-tdd

Then add django-tdd to your INSTALLED_APPS:

    INSTALLED_APPS = {
      ...
      'django_tdd',
    }

Usage
===

Use the management command in place of `runserver`. The following command will run all of the tests in your project and then start the development server.

    python manage.py tdd

When you change a file, the development server will stop, all the tests will be run again, and the development server will start again.
