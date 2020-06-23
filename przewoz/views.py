from django.shortcuts import render

APP_VERSION = '0.1'


# Create your views here.
def index(request):
    return render(request, 'base.html', {'app_version': APP_VERSION})
