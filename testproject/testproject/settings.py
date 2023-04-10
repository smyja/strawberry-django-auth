"""Django settings for testproj project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

from gqlauth.backends.strawberry_django_auth.backend import DjangoGqlAuthBackend
from gqlauth.settings_type import GqlAuthSettings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!d)n5m95oazv&40!i76&+2d5)r%om$2t%2i%w1^*o9*$%b9sm$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "gqlauth.backends.strawberry_django_auth",
    "customeuser",
    "sample",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "gqlauth.core.middlewares.django_jwt_middleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "testproject" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

ASGI_APPLICATION = "testproject.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "OPTIONS": {
            "timeout": 1000000,
        },
        "NAME": str(BASE_DIR / "db.sqlite3"),
        "TEST": {
            "NAME": "test_database",
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media"

# custom settings start here
EMAIL_HOST = "mail.privateemail.com"
EMAIL_HOST_USER = "diffrent_than_gqlauth_default@cccc.com"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
AUTH_USER_MODEL = "customeuser.SimpleCustomUser"

GQL_AUTH = GqlAuthSettings(
    BACKEND=DjangoGqlAuthBackend(),
    LOGIN_REQUIRE_CAPTCHA=True,
    REGISTER_REQUIRE_CAPTCHA=True,
    CAPTCHA_SAVE_IMAGE=True,
    SEND_ACTIVATION_EMAIL=False,
)
