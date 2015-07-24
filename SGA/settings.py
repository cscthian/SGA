from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = '$96a-z!pd*tn!z8kodyuo1)yg#)xjq)xbe=g&87vqkqwdz4$0)'

DEBUG = False
TEMPLATES_HOST = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.asistencia',
    'apps.users',
    'apps.pagos',
    'apps.matricula',
    'apps.notas',
    'apps.cursolibre',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SGA.urls'

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
                'apps.asistencia.context_processors.asignaturas',
            ],
        },
    },
]

WSGI_APPLICATION = 'SGA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7p3tigtkj9eq4',
        'USER': 'ysjwekxuaeyexr',
        'PASSWORD': '6kfZ3hfBANnkYdJQnjQlc1Fc9p',
        'HOST': 'ec2-107-21-125-143.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
AWS_STORAGE_BUCKET_NAME = 'iscunsaac'
AWS_ACCESS_KEY_ID = 'AKIAIGDFC2UACFQUO52A'
AWS_SECRET_ACCESS_KEY = '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'
STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = 'https://s3.amazonaws.com/iscunsaac/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MEDIA_ROOT = BASE_DIR.child('media')
