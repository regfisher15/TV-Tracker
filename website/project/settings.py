"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from interfaces import env
import os
import multiprocessing
from project.celery import beat_schedule

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


PARAMS = ["USER", "PASSWORD", "HOST", "PORT", "DATABASE",
          "DJANGO_SECURE_KEY", "DJANGO_PG_SCHEMA",
          "RHOST", "RPORT", "DEBUG"]
CONFIG = env.get(PARAMS, dont_assert=["DEBUG"])

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get("DJANGO_SECURE_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(CONFIG.get("DEBUG", False))

ALLOWED_HOSTS = ['tate-server.ddns.net']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # "debug_toolbar",
    'our_app',
    'accounts',
    "verify_email.apps.VerifyEmailConfig",
]

ROOT_URLCONF = 'project.urls'

AUTH_USER_MODEL = "accounts.CustomUser"

# LOGIN_REDIRECT_URL = "home"
# LOGOUT_REDIRECT_URL = "home"

UI_TEMPLATES = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [UI_TEMPLATES],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONFIG.get("DATABASE"),
        'USER': CONFIG.get("USER"),
        'PASSWORD': CONFIG.get("PASSWORD"),
        'HOST': CONFIG.get("HOST"),
        'PORT': CONFIG.get("PORT"),
        'OPTIONS': {
            'options': f'-c search_path={CONFIG.get("DJANGO_PG_SCHEMA")}'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = CONFIG.get("GMAIL")
EMAIL_HOST_PASSWORD = CONFIG.get("GMAILPSWD")

CSRF_TRUSTED_ORIGINS = [
    'https://localhost',
    'https://tate-server.ddns.net'
]



redis_host = CONFIG.get("RHOST")
redis_port = CONFIG.get("RPORT")

redis_uri = f"redis://{redis_host}:{redis_port}"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": redis_uri,
        "KEY_PREFIX" : "__django__",
    }
}

CACHE_TTL = 60 * 15

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

SESSION_COOKIE_AGE = 3600

CELERY_BROKER_URL = redis_uri
CELERY_RESULT_BACKEND = redis_uri

CELERY_BEAT_SCHEDULE = beat_schedule

CELERYD_CONCURRENCY = multiprocessing.cpu_count() * 2 + 1