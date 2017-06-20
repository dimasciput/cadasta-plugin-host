import os
from django.template import loader
from django.http import HttpResponse
from .models.plugin import Plugin
from .models.release import Release
from core.settings.utils import absolute_path
from django.conf import settings


def index(request):
    template = loader.get_template('plugin_index.html')
    context = {
        'plugins': Plugin.objects.all(),
        'releases': Release.objects.all()
    }
    return HttpResponse(template.render(context, request))


def plugin(request):
    template = loader.get_template('plugins.xml')
    releases = []

    plugins = Plugin.objects.all()

    for plug in plugins:
        release = Release.objects.filter(plugin=plug).order_by('-date')[0]
        releases.append(release)

    host_name = ''

    try:
        host_name = settings.PLUGINS_HOST
    except AttributeError:
        pass

    context = {
        'releases': releases,
        'host_name': host_name
    }
    return HttpResponse(
        template.render(context, request),
        content_type='application/xml'
    )
