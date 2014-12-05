# -*- coding: utf-8 -*-
"""Python packaging."""
import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(here)


NAME = 'django-sql-log-demo'
DESCRIPTION = ''
README = ''
VERSION = '0.0.0'
AUTHOR = u'Bruno Bord'
EMAIL = 'bruno.bord@novapost.fr'
URL = ''
CLASSIFIERS = []
KEYWORDS = []
PACKAGES = ['django_sql_log_demo']
REQUIREMENTS = [
    'django-sql-log',
    'setuptools',

]
ENTRY_POINTS = {
    'console_scripts': [
        'demo = django_sql_log_demo.manage:main',
    ]
}


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=README,
          classifiers=CLASSIFIERS,
          keywords=' '.join(KEYWORDS),
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license='BSD',
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=False,
          install_requires=REQUIREMENTS,
          entry_points=ENTRY_POINTS)
