"""
Django settings for cfb_api project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l2j(d08s0brvohw!wbw11!188%_#%$$!z54b)2lu72!y$-obw3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cfb_api.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'cfb_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WEBHOOK_WIKI_GRUPO1 = "https://discord.com/api/webhooks/1068658492698808450/8OPWJIg4Ba5jdEsDxqB48vWf9gMr16OiqbsLrb6y0hRnNS2kaB4A-hhVkBXc_rcRGqYg"
WEBHOOK_WIKI_GRUPO2 = "https://discord.com/api/webhooks/1068658650127806585/6ol0xyZb6IlPOABTL8WlU2ETI1mKzmTwDvVDzEfwf1DG9YoYewfvnZGQvZHrWtbDPQhz"
WEBHOOK_WIKI_GRUPO3 = "https://discord.com/api/webhooks/1068658761142640721/mgX7QI75cc8tLbwKr5-9c2la9StC43Xcl3gaUxQVyq9QLY2pjiO27uiMJJ3I6VycTk1C"
WEBHOOK_ISSUES = "https://discord.com/api/webhooks/1068659660074262619/X41fGJ2ixDN0-H3tCnxIZSMXxz1jWkZjOrP8QwNFKDO2hWieNZ8qMXobdUziazYr92zs"
WEBHOOK_ACTIONS = "https://discord.com/api/webhooks/1068659928589418506/jqj9Mrpmn9JvMiqrEOfJwUAoc3wRc6zPtYty56IJGi6Zfg77FB-6IGri9ozvWdlWYT8y"
WEBHOOK_CODACY = "https://discord.com/api/webhooks/1068972044177395852/O8-ING5IhOVu0OPK00PP9opOa5wqQO1_DOVLgTEisgZD3MeRw8_r_B_wBSiJ2B2w4Kh4"