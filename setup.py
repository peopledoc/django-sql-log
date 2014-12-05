# -*- coding: utf-8 -*-
"""Python packaging."""
import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

NAME = u'django-sql-log'
VERSION = '0.0.1'
README = 'Not ready yet'
DESCRIPTION = u'Loging made simple.'
PACKAGES = ['django_sql_log']
REQUIREMENTS = [
    'django<1.7',
]
AUTHOR = u'Novapost'
EMAIL = u'bruno.bord@novapost.fr'
URL = u''
CLASSIFIERS = []
KEYWORDS = []


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
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=False,
          install_requires=REQUIREMENTS,
          )
