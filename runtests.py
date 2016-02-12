#! /usr/bin/env python
import os
import sys

import django
from django.conf import settings

DIRNAME = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.getcwd())

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    INSTALLED_APPS=(
        'lightpdf',
    ),
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ),
    MEDIA_ROOT=os.path.join(DIRNAME, 'media'),
    MEDIA_URL='/media/',
    STATIC_ROOT=os.path.join(DIRNAME, 'static'),
    STATIC_URL='/static/',
)

try:
    django.setup()
except AttributeError:
    pass  # Django < 1.7; okay to ignore


from django.test.runner import DiscoverRunner


test_runner = DiscoverRunner(verbosity=2)
failures = test_runner.run_tests(['lightpdf'])
if failures:
    sys.exit(1)
