# -*- coding: utf-8 -*-
"""Python packaging."""
import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

NAME = u'django-sql-log'
VERSION = '1.1.0'
README = open(os.path.join(here, 'README.rst')).read()
DESCRIPTION = u'Write Start/Stop events in your SQL logs.'
PACKAGES = ['django_sql_log']
REQUIREMENTS = [
    'django<1.7',
]
AUTHOR = u'Novapost'
EMAIL = u'bruno.bord@novapost.fr'
URL = u'https://github.com/novapost/django-sql-log'
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database',
    'Topic :: System :: Logging',
]
KEYWORDS = ['django', 'SQL', 'log', 'postgresql']


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(
        name=NAME,
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
