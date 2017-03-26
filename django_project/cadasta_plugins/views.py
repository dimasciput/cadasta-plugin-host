import os
from django.template import loader
from django.http import HttpResponse
from .models.plugins import Plugin
from core.settings.utils import absolute_path


def index(request):
    template = loader.get_template('index.html')
    context = {
        'plugins': Plugin.objects.all()
    }
    return HttpResponse(template.render(context, request))


def repository(request):
    return HttpResponse(open(absolute_path('cadasta_plugins', 'static/plugins.xml')).xreadlines())
