import os

from django.http import HttpResponse

APP_NAME = "oxzoo-react-django"


def greeting(request):
    # Read at request time so the ox Environment editor can change the tag
    # without redeploying the frontend.
    tag = os.environ.get("GREETING_TAG", "")
    return HttpResponse(f"hello world {APP_NAME}_{tag}", content_type="text/plain")


def health(request):
    return HttpResponse("ok", content_type="text/plain")
