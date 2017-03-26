from django.template import loader
from django.http import HttpResponse
from .models.plugins import Plugin


def index(request):
    template = loader.get_template('index.html')
    context = {
        'plugins': Plugin.objects.all()
    }
    return HttpResponse(template.render(context, request))
