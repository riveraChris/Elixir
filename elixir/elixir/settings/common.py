"""
Common Django settings for the appointments project.

See the local, test, and production settings modules for the values used
in each environment.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&=uxu@^o#!c=wo3xan^a0$bmgg-p6h(a^urwiqksx!z-7%syr$'

# Most important settings

# Twilio API
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

# Address of Redis instance, our Celery broker
BROKER_URL = 'redis://localhost:6379/0'
BROKER_POOL_LIMIT = 8

# Reminder time: how early text messages are sent in advance of appointments
REMINDER_TIME = 1 # minutes

ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'django_forms_bootstrap',
    'timezone_field',
    'django_extensions',
    'django_filters',
    'annoying',
    'registration',
    'crispy_forms',
)

LOCAL_APPS = (
    'appointment',
    'treatment',
    'patient',
    'doctor',
    'record',
    'users',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

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

ROOT_URLCONF = 'elixir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

WSGI_APPLICATION = 'elixir.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elixir',
        'USER': 'chris',
        'PASSWORD': 'passw1rd',
        'HOST': 'localhost',
        'PORT': ''

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rivera2527@gmail.com'
DEFAULT_FROM_EMAIL = 'rivera2527@gmail.com'
SERVER_EMAIL = 'rivera2527@gmail.com'
EMAIL_HOST_PASSWORD = 'Labs2527'

LOGIN_REDIRECT_URL = '/hipaa'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR + '/staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, '../static'),)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, '../templates'),)
