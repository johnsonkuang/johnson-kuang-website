"""
Django settings for johnsonkuangwebsite project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import posixpath
from configparser import ConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if config.has_option('Django', 'SECRET_KEY'):
    SECRET_KEY = config.get('Django', 'SECRET_KEY')
else:
    # We should never be in production with this key
    SECRET_KEY = '8390cfc1-31c5-464e-ba9e-62071af75c3c'

# SECURITY WARNING: don't run with debug turned on in production!
#  we will default to True if not overriden in the config file
if config.has_option('Django', 'DEBUG'):
    DEBUG = config.getboolean('Django', 'DEBUG')
else:
    DEBUG = True

# TODO: Take this out when done debugging production
# DEBUG = True

if config.has_option('Django', 'ALLOWED_HOSTS'):
    USE_X_FORWARDED_HOST = True
    ALLOWED_HOSTS = config.get('Django', 'ALLOWED_HOSTS').split(',')
else:
    ALLOWED_HOSTS = []

#Email settings
EMAIL_BACKEND = config.get('Email', 'EMAIL_BACKEND')
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST = config.get('Email', 'EMAIL_HOST')
EMAIL_HOST_USER = config.get('Email', 'EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = config.get('Email', 'EMAIL_HOST_PASSWORD')
EMAIL_PORT = config.getint('Email', 'EMAIL_PORT')
EMAIL_USE_TLS = config.getboolean('Email', 'EMAIL_USE_TLS')

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'website',
    'blog',
    'taggit',
    'markdown',
    'widget_tweaks',
    'crispy_forms',
    'control_panel',
    'accounts',
    'lockdown',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'image_cropping',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
if DEBUG:
    #if debugging change this value to control number of seconds sessions last
    SESSION_EXPIRE_SECONDS = 300
else:
    SESSION_EXPIRE_SECONDS = config.getint('Session', 'SESSION_EXPIRE_SECONDS')
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

LOCKDOWN_PASSWORDS = (config.get('Lockdown', 'LOCKDOWN_PASSWRODS'),)

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}

ROOT_URLCONF = 'johnsonkuangwebsite.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'johnsonkuangwebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if ALLOWED_HOSTS:
    DATABASES = {
        'default': {
            'ENGINE': config.get('Postgres', 'ENGINE'),
            'NAME': config.get('Postgres', 'NAME'),
            'USER': config.get('Postgres', 'USER'),
            'PASSWORD': config.get('Postgres', 'PASSWORD'),
            'HOST': config.get('Postgres', 'HOST'),
            'PORT': config.get('Postgres', 'PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_PROFILE_MODULE = 'accounts.Profile'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

MEDIA_URL = '/media/'

MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media']))

#accounts
LOGIN_REDIRECT_URL = 'website:index'