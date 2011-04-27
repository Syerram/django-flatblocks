import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, os.path.dirname(PROJECT_ROOT))

DEBUG=True
TEMPLATE_DEBUG=True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/flatblocks.db'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'flatblocks',
]
try:
    import south
    INSTALLED_APPS.append('south')
except ImportError, _:
    pass

LANGUAGE_CODE="en"
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
ROOT_URLCONF = 'test_project.urls'
