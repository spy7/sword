"""
Django settings for be_sword project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os

from pathlib import Path

from pythonjsonlogger.jsonlogger import JsonFormatter

from be_sword.utils import strtobool

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.getenv("DJANGO_DEBUG", "True"))

DJANGO_ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS")

ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS.split(",") if DJANGO_ALLOWED_HOSTS else ["*"]

# CSRF
CSRF_TRUSTED_ORIGINS: list[str] | str
if CSRF_TRUSTED_ORIGINS := os.getenv("CSRF_TRUSTED_ORIGINS", ""):
    CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS.split(",")

CSRF_COOKIE_SECURE = strtobool(os.getenv("CSRF_COOKIE_SECURE", "False"))
SESSION_COOKIE_SECURE = strtobool(os.getenv("SESSION_COOKIE_SECURE", "False"))

# CORS
CORS_ALLOWED_ORIGINS: list[str] | str
if CORS_ALLOWED_ORIGINS := os.getenv("CORS_ALLOWED_ORIGINS", ""):
    CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS.split(",")
else:
    CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "book",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "be_sword.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "be_sword.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if strtobool(os.getenv("DB_LOCAL", "True")):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.getenv("DB_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.getenv("DB_USER"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
        }
    }

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "drf_link_navigation_pagination.LinkNavigationPagination",
    "PAGE_SIZE": int(os.getenv("PAGE_SIZE", 30)),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_MOCK = strtobool(os.getenv("EMAIL_MOCK", "True"))
if EMAIL_MOCK:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = strtobool(os.getenv("EMAIL_USE_TLS", "False"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "host_user@example.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "host_password")
EMAIL_SYSTEM_ADMIN = os.getenv("EMAIL_SYSTEM_ADMIN", "sysadmin@example.com")
EMAIL_UPLOAD_SUBJECT = os.getenv("EMAIL_UPLOAD_SUBJECT", "Books uploaded")
EMAIL_UPLOAD_MESSAGE = os.getenv(
    "EMAIL_UPLOAD_MESSAGE", "%s books uploaded successfully"
)
EMAIL_UPLOAD_FAIL = os.getenv("EMAIL_UPLOAD_FAIL", "Invalid books:")
EMAIL_INVALID_FILE_MESSAGE = os.getenv(
    "EMAIL_INVALID_FILE_MESSAGE", "Invalid file format"
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "()": JsonFormatter,
            "format": "%(levelname)-8s [%(asctime)s]: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": os.getenv("DEFAULT_LOG_FORMATTER", "standard"),
        }
    },
    "loggers": {
        "": {"level": os.getenv("ROOT_LOG_LEVEL", "INFO"), "handlers": ["console"]},
        "be_sword": {
            "level": os.getenv("PROJECT_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
        "django": {
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
        },
        "django.db.backends": {
            "level": os.getenv("DJANGO_DB_BACKENDS_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
        },
        "django.request": {
            "level": os.getenv("DJANGO_REQUEST_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
        },
    },
}
