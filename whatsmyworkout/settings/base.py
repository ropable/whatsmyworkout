"""
Django settings for whatsmyworkout project.
Call and extend these settings by passing --settings=<PATH> to runserver, e.g.

    python manage.py runserver --settings=tickit_project.settings.base
"""
import os
import sys
from unipath import Path
import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Project paths
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).ancestor(3)
PROJECT_DIR = os.path.join(BASE_DIR, 'whatsmyworkout')
# Add PROJECT_DIR to the system path.
sys.path.insert(0, PROJECT_DIR)

# Application definition
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = []
ROOT_URLCONF = 'whatsmyworkout.urls'
WSGI_APPLICATION = 'whatsmyworkout.wsgi.application'

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'django_extensions',
    'django_wsgiserver',
    # Projects apps
    'exercise',
    'workout',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]


# Database
DATABASES = {'default': dj_database_url.config()}


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'whatsmyworkout', 'static'),
)


# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/whatsmyworkout.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 Mb
            'backupCount': 5,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/django_request.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 Mb
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


# Authentication
AUTH_USER_MODEL = 'workout.WorkoutUser'
ANONYMOUS_USER_ID = -1
#LOGIN_REDIRECT_URL = '/'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
