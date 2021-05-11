import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'au#5!nni%&0@&s=8+igfdz5n8l-7^s+@=snu-u#ip=92&vd8on'

DEBUG = True

ALLOWED_HOSTS = ["web", "127.0.0.1", "localhost"]


INSTALLED_APPS = [
    'music.apps.MusicConfig',
    'taggit', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'django.contrib.sites',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'playlist.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account'
            ],
        },
    },
]

WSGI_APPLICATION = 'playlist.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "/account/login/"

LOGIN_REDIRECT_URL = "index" 

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ACCOUNT_EMAIL_UNIQUE = True

ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

ACCOUNT_LOGIN_URL = 'account_login'

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = ACCOUNT_LOGIN_URL

ACCOUNT_PASSWORD_RESET_REDIRECT_URL = ACCOUNT_LOGIN_URL

ACCOUNT_EMAIL_CONFIRMATION_URL = "account_confirm_email"

ACCOUNT_SETTINGS_REDIRECT_URL = "account_settings"

ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "account_password"

SITE_ID = 2

AUTHENTICATION_BACKENDS = [
    'account.auth_backends.EmailAuthenticationBackend',
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.getenv('HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('FROM_EMAIL')
