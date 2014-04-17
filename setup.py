#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from setuptools import setup
import os
import re


def abs_path(relative_path):
    """
    Given a path relative to this directory return an absolute path.
    """
    base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)


def get_version(relative_path):
    """
    Return version given package's path.
    """
    data = open(os.path.join(abs_path(relative_path), '__init__.py')).read()
    return re.search(r"__version__ = '([^']+)'", data).group(1)


def get_long_description():
    """
    Return the contents of the README file.
    """
    try:
        return open(abs_path('README.md')).read()
    except:
        pass  # Required to install using pip (won't have README then)


setup(
    name='django-tdd',
    version=get_version('django_tdd'),
    description='A continuous test runner for Django',
    long_description=get_long_description(),
    author='Kevin Harvey',
    author_email='kcharvey@gmail.com',
    url='https://github.com/kcharvey/django-tdd',
    packages=('django_tdd',
              'django_tdd.management',
              'django_tdd.management.commands'),
    license='Public Domain',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)
