=======
Plugins
=======

Plugins is a simple Django app to host qgis polls.

Quick start
-----------

1. Add "plugins" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'plugins',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^kartoza_plugins/', include('plugins.urls')),

3. Run `python manage.py migrate` to create the plugins models.
