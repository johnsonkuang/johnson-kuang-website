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

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8390cfc1-31c5-464e-ba9e-62071af75c3c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'johnsonqkuang@gmail.com'

EMAIL_HOST_PASSWORD = 'h"dhC\!KD[FN%u(.+rpTp,Q\'\Cs\'J&)-Ka\'K>6yq'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'website',
    'blog',
    'taggit',
    'markdown',
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

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'devtest',
        'USER': 'johnson',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'kuang-ubuntu.westus.cloudapp.azure.com',
        'PORT': '5432',
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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

MEDIA_URL = '/media/'

MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media']))