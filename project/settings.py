"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from google.oauth2 import service_account
#from decouple import config
# from dj_database_url import parse as dburl
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h=lg=b67yj$grv0_rkt7q-d08u-(@=5#0+k2$r@0j!orn#4yx('
# SECRET_KEY =config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'social_django',
    'corsheaders', 
    'django_filters',
    'childrenhealthcare',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CORS_ALLOWED_ORIGINS = [
#         "https://example.com",
#         "https://sub.example.com",
#         "http://localhost:8080",
#         "http://127.0.0.1:9000"
#     ]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'project.urls'

REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES': 
                ('rest_framework.authentication.TokenAuthentication',
                'rest_framework.authentication.SessionAuthentication'),

'DEFAULT_PERMISSION_CLASSES':[
'rest_framework.permissions.AllowAny',
],}
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
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
# DATABASES = {
#     'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Project',
#         'USER': 'postgres',
#         'PASSWORD': 'PGinfm@20320',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# }

# AUTH_USER_MODEL = 'childernhealthcare.CustomAdmin'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
  ('ar', ('Arabic')),
  ('en', ('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
MEDIA_URL = 'media/'
# MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = '/Viewsets/Sections'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'a.01092664268@gmail.com'
EMAIL_HOST_PASSWORD = 'dqxdkhluxynynfts'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
for key in ['GOOGLE_OAUTH2_KEY',
            'GOOGLE_OAUTH2_SECRET',
            'FACEBOOK_KEY',
            'FACEBOOK_SECRET']:
    # Use exec instead of eval here because we're not just trying to evaluate a dynamic value here;
    # we're setting a module attribute whose name varies.
    exec("SOCIAL_AUTH_{key} = os.environ.get('{key}')".format(key=key))


SOCIAL_AUTH_PIPELINE = (
  'social_core.pipeline.social_auth.social_details',
  'social_core.pipeline.social_auth.social_uid',
  'social_core.pipeline.social_auth.auth_allowed',
  'social_core.pipeline.social_auth.social_user',
  'social_core.pipeline.user.get_username',
  'social_core.pipeline.social_auth.associate_by_email',
  'social_core.pipeline.user.create_user',
  'social_core.pipeline.social_auth.associate_user',
  'social_core.pipeline.social_auth.load_extra_data',
  'social_core.pipeline.user.user_details',
)

