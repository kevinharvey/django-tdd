django-tdd
==========

A Django management command to run tests every time a file is saved.

Installation
===

    pip install django-tdd

Then add django-tdd to your INSTALLED_APPS:

    INSTALLED_APPS = {
      ...
      'django-tdd',
    }

Usage
===

Use the management command in place of `runserver`. The following command will run all of the tests in your project (including the tests for Django itself), and then start the development server.

    python manage.py tdd

When you change a file, the development server will stop, all the tests will be run again, and the development server will start again.

The command is most helpful when you are working on a single app in a larger project and only want to run it's tests.

    python manage.py tdd myapp

Or if you want to run a single test case, or one single test

    python manage.py tdd myapp.MyTestCase
    python manage.py tdd myapp.MyTestCase.my_specific_test

