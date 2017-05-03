import os
from django.template import loader
from django.http import HttpResponse
from .models.plugin import Plugin
from core.settings.utils import absolute_path


def index(request):
    template = loader.get_template('index.html')
    context = {
        'plugins': Plugin.objects.all()
    }
    return HttpResponse(template.render(context, request))


def plugin(request):
    xml_data = open(absolute_path('cadasta_plugins', 'static/plugins.xml'), "rb").read()
    return HttpResponse(
        xml_data,
        content_type='application/xml'
    )
