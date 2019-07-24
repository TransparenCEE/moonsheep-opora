from .base import *

DEBUG = True

SECRET_KEY = 'whateva'

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
    MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = [
    '127.0.0.1',
]

# MOONSHEEP_TASK_SOURCE = 'random'
# MOONSHEEP_DEVELOPMENT_MODE = True
