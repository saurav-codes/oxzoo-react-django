import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Real deployments set DJANGO_SECRET_KEY in the ox Environment editor.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-example-key")

DEBUG = False

ALLOWED_HOSTS = ["react-django.oxzoo.sorv.dev", "127.0.0.1", "localhost"]

# No models and no admin in this example, so no apps are installed.
INSTALLED_APPS = []

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "hello.urls"

TEMPLATES = []

WSGI_APPLICATION = "hello.wsgi.application"

# This example has no models, so no database is configured and the deploy
# manifest needs no migrate hook. A sqlite file would also be unwritable at
# runtime under the ox sandbox.
DATABASES = {}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
