"""
Django settings for medstat project.

Generated by 'django-admin startproject' using Django 3.0.5.

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0jk#7%8@iomx*0(%ydx9jv8i#b83rp#x4!u17kq)2-e%@u*n*n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'articles.apps.ArticlesConfig',
    'users.apps.UsersConfig',
    # 'social.apps.django_app.default',  # https://pocoz.gitbooks.io/django-v-primerah/glava-4-sozdanie-social-website/avtorizatsiya-cherez-sotsialnie-seti.html
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',  # Фреймворк аутентификации и моделей по умолчанию
    'django.contrib.contenttypes',  # Django контент-типовая система (даёт разрешения, связанные с моделями)
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'rest_framework',
]
# Социальные сети
# https://evileg.com/ru/post/11/
# https://evileg.com/ru/post/420/ FB
# https://webdevblog.ru/django-autentifikaciya-s-facebook-instagram-i-linkedin/
# https://developers.facebook.com/docs/facebook-login/web#logindialog.

# https://fbgid.ru/faq/kak-sdelat-ssylku-na-stranitsu-v-fejsbuk

# https://evileg.com/ru/post/367/ VK
# pip install social-auth-app-django
# python manage.py migrate
# PostgreSQL...

MIDDLEWARE = [
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Должен быть первым, чтобы полностью замерять используемое время, память и т.д.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Управление сессиями между запросами
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Связывает пользователей, использующих сессии, запросами
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medstat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'medstat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

# Инсталяция https://www.django-rest-framework.org/#installation
# Другие приложения https://djangopackages.org/grids/g/django-rest-framework/
# Чтобы незарегистрированные пользователи могли пользоваться API
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }
# Пагинация страниц API
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

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
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [
#     'medstat/articles/static',
# ]

# определение места хранения фотографий
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Переопределение класса пользователя
AUTH_USER_MODEL = 'users.ArticlesUser'

# Редиректы при регистрации/выходе
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/users/login'

# https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
# Development
# Для тестирования https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Аутентификация
# Console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#  suggests the dummy backend
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# https://docs.djangoproject.com/en/2.0/topics/email/#smtp-backend
# Production
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'test@test.com'
# EMAIL_HOST_PASSWORD = 'test'
# EMAIL_PORT = 587

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]