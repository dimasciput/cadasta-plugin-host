from django.conf.urls import url, patterns
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
