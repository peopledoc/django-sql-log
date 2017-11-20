# django-sql-log

## master (unreleased)

* Added a few tests using query count - assertNumQueries (#19).
* Fixed template settings for Django 1.8 and later (#22).

## 1.2.1 (2015-06-10)

* Fixed unwanted warnings in Django 1.7 tests (#14)
* Travis tests build with Postgresql and up to the latest Django version (#13).

## 1.2.0 (2015-06-09)

* Picked up License (MIT)
* Travis build is ready.
* `django-sql-log` is now ready for Django 1.6, 1.7, 1.8, thanks to tox.

## 1.1.0 (2014-12-08)

(yes, that's 3 releases on the same day).

* Merging middlewares. We used to have two middlewares to handle requests (start) and responses (stop). Now everything is handled by a single middleware.

## 1.0.1 (2014-12-08)

Bugfixes:

* Do not break on 404 pages,
* Do not break on 500 pages.

## 1.0.0 (2014-12-08)

First public release.

* Basic functionality, just set these middlewares up, and you can have Start/Stop markers in your database log,
* This module has been tested along with Postgresql / SQLite and Django 1.6.
