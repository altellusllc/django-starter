from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    "aigraphgenerator.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://aigraphgenerator.com",
]

CORS_ALLOWED_ORIGINS = [
    "https://aigraphgenerator.com",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
    }
}

STATIC_ROOT = "/var/www/html/static"
STATIC_URL = "/static/"
MEDIA_ROOT = "/var/www/html/media"
MEDIA_URL = "/media/"
STATICFILES_DIRS = [
    "/home/webapp/static",
]

SITE_ROOT = "https://aigraphgenerator.com"
BASE_URL = "https://aigraphgenerator.com"

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")


EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "syslog": {
            "level": "DEBUG",
            "class": "logging.handlers.SysLogHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/uwsgi/django.log",
        },
    },
    "formatters": {
        "rich": {"datefmt": "[%Y-%m-%d %X]"},
        "simple": {
            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s]: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
    },
    # Set 'propagate' to False to prevent duplicate logging
    "loggers": {
        "django.request": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "core": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


# Allauth settings
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
