from django.http import HttpResponse
from . import apps
# Create your views here.

def show(request):
    return HttpResponse(apps.Application1Config.name)