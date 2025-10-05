import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env (optional for local dev)
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Hosts allowed to serve your app
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mytutorapp',  # Your custom app
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

ROOT_URLCONF = 'kgt_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project-level templates folder
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

WSGI_APPLICATION = 'kgt_website.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'kgt_db'}")
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Optional for local development
STATIC_ROOT = BASE_DIR / 'staticfiles'    # For collectstatic in production

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URL
LOGIN_URL = '/login/'

# from pathlib import Path
# import os
# import dj_database_url

# # Base directory
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Secret Key
# SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")

# # Debug mode
# DEBUG = os.environ.get("DEBUG", "False") == "True"

# # Allowed hosts
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# # Media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'mediafiles'

# # Installed apps
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'mytutorapp',
# ]

# # Middleware
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # URLs and WSGI
# ROOT_URLCONF = 'kgt_website.urls'
# WSGI_APPLICATION = 'kgt_website.wsgi.application'

# # Templates
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # Database (SQLite default, use Postgres on Render if desired)
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'kgt_db'}")
#     )
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_TZ = True

# # Static files
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# # Default primary key
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Login URL
# LOGIN_URL = '/login/'

# from pathlib import Path
# import os
# import dj_database_url

# # ---------------------------
# # Base directory
# # ---------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # ---------------------------
# # Security
# # ---------------------------
# SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")
# DEBUG = os.environ.get("DEBUG", "False") == "True"
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# # ---------------------------
# # Applications
# # ---------------------------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'mytutorapp',  # Your app
# ]

# # ---------------------------
# # Middleware
# # ---------------------------
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # ---------------------------
# # URLs and WSGI
# # ---------------------------
# ROOT_URLCONF = 'kgt_website.urls'

# WSGI_APPLICATION = 'kgt_website.wsgi.application'

# # ---------------------------
# # Templates
# # ---------------------------
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # ---------------------------
# # Database
# # ---------------------------
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'kgt_db'}")
#     )
# }

# # ---------------------------
# # Password validation
# # ---------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

# # ---------------------------
# # Internationalization
# # ---------------------------
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_TZ = True

# # ---------------------------
# # Static & Media files
# # ---------------------------
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]  # Local dev
# STATIC_ROOT = BASE_DIR / 'staticfiles'   # Production collectstatic

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'mediafiles'

# # ---------------------------
# # Default primary key
# # ---------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # ---------------------------
# # Login
# # ---------------------------
# LOGIN_URL = '/login/'

# # from pathlib import Path
# # import os
# # import dj_database_url  # Make sure you have this in requirements.txt

# # # Build paths inside the project like this: BASE_DIR / 'subdir'
# # BASE_DIR = Path(__file__).resolve().parent.parent

# # # SECURITY WARNING: keep the secret key used in production secret!
# # SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")

# # # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = os.environ.get("DEBUG", "True") == "True"

# # # Allow hosts from environment variable, default to Render URL or '*'
# # ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# # # Media files
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = BASE_DIR / 'mediafiles'

# # # Application definition
# # INSTALLED_APPS = [
# #     'django.contrib.admin',
# #     'django.contrib.auth',
# #     'django.contrib.contenttypes',
# #     'django.contrib.sessions',
# #     'django.contrib.messages',
# #     'django.contrib.staticfiles',
# #     'mytutorapp',  # Your custom app
# # ]

# # MIDDLEWARE = [
# #     'django.middleware.security.SecurityMiddleware',
# #     'django.contrib.sessions.middleware.SessionMiddleware',
# #     'django.middleware.common.CommonMiddleware',
# #     'django.middleware.csrf.CsrfViewMiddleware',
# #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# #     'django.contrib.messages.middleware.MessageMiddleware',
# #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # ]

# # ROOT_URLCONF = 'kgt_website.urls'

# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': [BASE_DIR / 'templates'],
# #         'APP_DIRS': True,
# #         'OPTIONS': {
# #             'context_processors': [
# #                 'django.template.context_processors.debug',
# #                 'django.template.context_processors.request',
# #                 'django.contrib.auth.context_processors.auth',
# #                 'django.contrib.messages.context_processors.messages',
# #             ],
# #         },
# #     },
# # ]

# # WSGI_APPLICATION = 'kgt_website.wsgi.application'

# # # Database
# # DATABASES = {
# #     'default': dj_database_url.config(
# #         default=os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'kgt_db'}")
# #     )
# # }

# # # Password validation
# # AUTH_PASSWORD_VALIDATORS = [
# #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
# #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
# #     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
# #     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# # ]

# # # Internationalization
# # LANGUAGE_CODE = 'en-us'
# # TIME_ZONE = 'Asia/Kolkata'
# # USE_I18N = True
# # USE_TZ = True

# # # Static files (CSS, JavaScript, Images)
# # STATIC_URL = '/static/'
# # STATICFILES_DIRS = [BASE_DIR / "static"]  # Optional for local dev
# # STATIC_ROOT = BASE_DIR / 'staticfiles'     # Used for collectstatic in production

# # # Default primary key field type
# # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # # Login redirect
# # LOGIN_URL = '/login/'

# # Django settings for kgt_website project.

# # Generated by 'django-admin startproject' using Django 5.1.7.

# # For more information on this file, see
# # https://docs.djangoproject.com/en/5.1/topics/settings/

# # For the full list of settings and their values, see
# # https://docs.djangoproject.com/en/5.1/ref/settings/
# # """

# # from pathlib import Path

# # # Build paths inside the project like this: BASE_DIR / 'subdir'.
# # BASE_DIR = Path(__file__).resolve().parent.parent


# # # Quick-start development settings - unsuitable for production
# # # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# # # SECURITY WARNING: keep the secret key used in production secret!
# # SECRET_KEY = 'django-insecure-d8!^9*5xb18q@q@mott@2r-@a)p#9w(ltt-=+blf-+zpu+uf(m'

# # # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = True

# # ALLOWED_HOSTS = []


# # # Application definition

# # INSTALLED_APPS = [
# #     'django.contrib.admin',
# #     'django.contrib.auth',
# #     'django.contrib.contenttypes',
# #     'django.contrib.sessions',
# #     'django.contrib.messages',
# #     'django.contrib.staticfiles',
# #     'mytutorapp',
# # ]

# # MIDDLEWARE = [
# #     'django.middleware.security.SecurityMiddleware',
# #     'django.contrib.sessions.middleware.SessionMiddleware',
# #     'django.middleware.common.CommonMiddleware',
# #     'django.middleware.csrf.CsrfViewMiddleware',
# #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# #     'django.contrib.messages.middleware.MessageMiddleware',
# #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # ]

# # ROOT_URLCONF = 'kgt_website.urls'

# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': [BASE_DIR / 'templates'], 
# #         'APP_DIRS': True,
# #         'OPTIONS': {
# #             'context_processors': [
# #                 'django.template.context_processors.debug',
# #                 'django.template.context_processors.request',
# #                 'django.contrib.auth.context_processors.auth',
# #                 'django.contrib.messages.context_processors.messages',
# #             ],
# #         },
# #     },
# # ]

# # WSGI_APPLICATION = 'kgt_website.wsgi.application'


# # # Database
# # # https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / 'db.sqlite3',
# #     }
# # }


# # # Password validation
# # # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# # AUTH_PASSWORD_VALIDATORS = [
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# #     },
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# #     },
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# #     },
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# #     },
# # ]


# # # Internationalization
# # # https://docs.djangoproject.com/en/5.1/topics/i18n/

# # LANGUAGE_CODE = 'en-us'

# # TIME_ZONE = 'UTC'

# # USE_I18N = True

# # USE_TZ = True


# # # Static files (CSS, JavaScript, Images)
# # # https://docs.djangoproject.com/en/5.1/howto/static-files/

# # STATIC_URL = 'static/'

# # # Default primary key field type
# # # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# """
# Django settings for kgt_website project.
# Generated by 'django-admin startproject' using Django 5.x
# """
