"""
Django settings for quacker project.

<<<<<<< HEAD
Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jm=l&92gr^4!x8&#8)!+7c-!p6jzkw@5&vi7zo=^4sr*kohkv+'
=======
Generated by 'django-admin startproject' using Django 4.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(7tz%crv^pteqc$^24z&%v))%k8pintn8bcc@6oo^)cqq@zkl!'
>>>>>>> 7a59026 (Final Sprint)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['quacker.com', 'localhost', '127.0.0.1']
=======
ALLOWED_HOSTS = ['quacker.com','127.0.0.1']

# AUTHENTICATION_BACKENDS = ['social_auth.backends.facebook.FacebookOAuth2','django.contrib.auth.backends.ModelBackend',]

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'newsapp.authentication.EmailAuthBackend',
                           'social_core.backends.facebook.FacebookOAuth2',
                           'social_core.backends.google.GoogleOAuth2',
                           ]

SOCIAL_AUTH_FACEBOOK_KEY = '1473187433187351' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '99136b0cb98bb2967d3cf395df098820' # Facebook App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '421794033523-flgke4jgcdgn1anqupl30lmrkmrfv404.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' # Google Consumer Secret


>>>>>>> 7a59026 (Final Sprint)

# Application definition

INSTALLED_APPS = [
<<<<<<< HEAD
    'newsapp.apps.NewsappConfig',
=======
    'daphne',
    'newsapp.apps.NewsappConfig',
    'chat.apps.ChatConfig',
>>>>>>> 7a59026 (Final Sprint)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
<<<<<<< HEAD
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '1473187433187351' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '99136b0cb98bb2967d3cf395df098820' # Facebook App Secret
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '421794033523-flgke4jgcdgn1anqupl30lmrkmrfv404.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' # Google Consumer Secret

=======
    'easy_thumbnails',
    'common',
    'channels',
]

>>>>>>> 7a59026 (Final Sprint)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quacker.urls'

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

WSGI_APPLICATION = 'quacker.wsgi.application'
<<<<<<< HEAD

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
=======
ASGI_APPLICATION = 'quacker.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
>>>>>>> 7a59026 (Final Sprint)

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
<<<<<<< HEAD
        'NAME': 'Quacker',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
=======
        'NAME': 'QuackerNews',
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
>>>>>>> 7a59026 (Final Sprint)

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

<<<<<<< HEAD
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
=======

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
>>>>>>> 7a59026 (Final Sprint)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

<<<<<<< HEAD
USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

=======
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> 7a59026 (Final Sprint)
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

<<<<<<< HEAD

=======
ABSOLUTE_URL_OVERRIDES = {
    'auth.user':lambda u:reverse_lazy('user_detail',args=[u.username])
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'quacker.blackshark@gmail.com'
EMAIL_HOST_PASSWORD = 'ugehjzqrwsssgbvv'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CHANNEL_LAYERS={
    'default':{
        'BACKEND':'channels.layers.InMemoryChannelLayer',
    }
}
>>>>>>> 7a59026 (Final Sprint)
