"""
Django settings for oceanic_keto project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_CHARSET = 'utf-8'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bgq8w487vf#7bq@h1dgv!4bc!go7s-x67_ac)lz#7eoao85-2='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS = ["*"]




# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'debug_toolbar',  # Подключение debug_toolbar
    'markdown',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'keto.apps.KetoConfig',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oceanic_keto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'oceanic_keto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
LOGIN_REDIRECT_URL = '/users/thanks/'
AUTH_USER_MODEL = 'auth.User'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки для Django Debug Toolbar
# Устанавливайте при помощи debug_toolbar.urls.
# Добавьте debug_toolbar в INSTALLED_APPS.
# А также добавьте группу 1 из INTERNAL_IPS.
# Дополнительные инструкции: https://django-debug-toolbar.readthedocs.io/
DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',

    }
}
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Стандартный бекенд для аутентификации по username
    'users.authentication.EmailAuthBackend',      # Наш кастомный бекенд для аутентификации по email
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTH_USER_MODEL = 'auth.User'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
