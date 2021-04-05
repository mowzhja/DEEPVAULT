"""
Django settings for DEEPVAULT project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY = os.environ['DJ_KEY']

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'users.apps.UsersConfig',
    'vault.apps.VaultConfig',
    'token_manager.apps.TokenManagerConfig',
    'crispy_forms',
    'rules',
    'axes'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware'
]

# Session settings
# https://docs.djangoproject.com/en/3.0/topics/http/sessions/

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ROOT_URLCONF = 'DEEPVAULT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'DEEPVAULT.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': 'localhost',
        'PORT': 9863
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Authentication backends
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/

AUTHENTICATION_BACKENDS = ['axes.backends.AxesBackend',
                           'rules.permissions.ObjectPermissionBackend',
                           'DEEPVAULT.backends.FernetBackend']

# Password hashers
# https://docs.djangoproject.com/en/3.0/topics/auth/passwords/

PASSWORD_HASHERS = [
    'DEEPVAULT.hashers.HardenedArgon2Hasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Misc. stuff

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'vault_home'
LOGIN_URL = 'login'

# Misc. security settings
# https://docs.djangoproject.com/en/3.1/topics/security/
# https://wiki.mozilla.org/Security/Server_Side_TLS

CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = 'no-referrer'

# django-axes configuration
# https://django-axes.readthedocs.io/en/latest/4_configuration.html

AXES_ENABLED = True
AXES_FAILURE_LIMIT = 4
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = 24  # hours
AXES_LOCK_OUT_BY_USER_OR_IP = True
AXES_USE_USER_AGENT = True
AXES_LOGGER = None
AXES_DISABLE_ACCESS_LOG = True
AXES_NEVER_LOCKOUT_GET = False
AXES_COOLOFF_MESSAGE = 'You have been locked out due to too requests. Retry in <b>24 hours</b>.'



