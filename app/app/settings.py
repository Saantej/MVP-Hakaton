"""
Django settings for ekomuz project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

import boto3

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='localhost').split(' ')

CSRF_TRUSTED_ORIGINS = ['https://team-3-10.tltpro.org', 'https://team-3-10-stage.tltpro.org', 'https://team-3-10-dev.tltpro.org']
# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_admin_listfilter_dropdown',
    'rest_framework',
    'storages',
    'drf_spectacular',
    'corsheaders',
]

PROJECT_APPS = [
    'user',
    'main',
    'regions',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS


LOGIN_URL = '/login/'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROLLBAR = {
    'access_token': os.getenv('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASS'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

# REDIS & CACHES & CELERY SETTINGS
REDIS_HOST = os.getenv('redis_host')
REDIS_PORT = os.getenv('redis_port')

REDIS = f"redis://{REDIS_HOST}:{REDIS_PORT}"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS,
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AWS_ACCESS_KEY_ID = os.getenv('S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('S3_SECRET_ACCESS_KEY')
AWS_S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
S3_USE_SSL = os.getenv('S3_USE_SSL') == 'True'

USE_S3 = os.getenv('USE_S3') == 'True'


BUCKET_NAME_DELIMITER = os.getenv('BUCKET_NAME_DELIMITER', '-')
BRANCH = os.getenv('BRANCH', 'dev')
BACKUP_BRANCH = os.getenv('BACKUP_BRANCH', 'main')
BUCKET_NAME_PREFIX = os.getenv('BUCKET_NAME_PREFIX', 'app')
PREFIX = BUCKET_NAME_PREFIX + BUCKET_NAME_DELIMITER

DEFAULT_FILE_STORAGE = 'app.settings.MediaStorage'

# AWS_S3_ENDPOINT_URL = 'https://storage.sales.ekom.uz'

S3_CLIENT = boto3.client('s3',
                         use_ssl=S3_USE_SSL,
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         endpoint_url=AWS_S3_ENDPOINT_URL
                         )

MEDIA_FOLDER_NAME = os.getenv('MEDIA_FOLDER_NAME')

STATIC_BUCKET_NAME = PREFIX + 'static' + BUCKET_NAME_DELIMITER + BRANCH
MEDIA_BUCKET_NAME = PREFIX + 'media' + BUCKET_NAME_DELIMITER + BRANCH

DEFAULT_FILE_STORAGE = 'app.storages.MediaStorage'

if USE_S3:
    STATIC_URL = f"{os.getenv('S3_ENDPOINT_URL')}/{STATIC_BUCKET_NAME}/"
    STATICFILES_STORAGE = 'app.storages.StaticStorage'
else:
    STATIC_URL = '/static/'

USE_STATIC_ROOT = os.getenv('USE_STATIC_ROOT') == 'True'
if USE_STATIC_ROOT:
    STATIC_ROOT = Path(BASE_DIR).joinpath('static').resolve()
else:
    STATICFILES_DIRS = (BASE_DIR / 'static',)



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

MENU_BUTTON_RENDER_PERMISSIONS_START = 'perm_access'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    "TITLE": "MVPhakaton",
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
    'SERVE_INCLUDE_SCHEMA': False,
}

# If using Docker the following will set your INTERNAL_IPS correctly in Debug mode:
if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


AUTH_USER_MODEL = 'user.User'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']


