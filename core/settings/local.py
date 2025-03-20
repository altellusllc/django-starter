from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "100.93.58.95",
    "boneyard",
    "boneyard.tail67c884.ts.net",
    "localhost",
    "127.0.0.1",
]

INTERNAL_IPS = [
    "100.77.220.121",
    "100.91.251.29",
    "100.90.125.9",
]

CSRF_TRUSTED_ORIGINS = [
    "http://100.93.58.95",
    "http://boneyard",
    "http://boneyard.tail67c884.ts.net",
    "http://localhost:8001",
    "http://127.0.0.1:8001",
]

CSRF_COOKIE_SECURE = False

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",
    "django_browser_reload",
]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

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
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "core": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
MEDIA_ROOT = "media"
MEDIA_URL = "media/"
BASE_URL = "http://100.93.58.95:8000"
SITE_ROOT = "http://100.93.58.95:8000"
