import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Deployments set DJANGO_SECRET_KEY as an ox variable (Generate on the review screen).
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-example-key")

DEBUG = False

# ox provides PUBLIC_HOST, the address the project serves. ALLOWED_HOSTS
# (comma-separated) overrides it, for example to add a second domain.
ALLOWED_HOSTS = [
    host.strip()
    for host in (
        os.environ.get("ALLOWED_HOSTS")
        or ",".join(filter(None, [os.environ.get("PUBLIC_HOST"), "127.0.0.1", "localhost"]))
    ).split(",")
    if host.strip()
]

# No models and no admin in this example, so no apps are installed.
INSTALLED_APPS = []

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "hello.urls"

TEMPLATES = []

WSGI_APPLICATION = "hello.wsgi.application"

# This example has no models, so no database is configured and the deploy
# manifest needs no migrate step.
DATABASES = {}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
