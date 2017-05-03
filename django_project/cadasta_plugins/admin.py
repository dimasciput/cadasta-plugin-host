from django.contrib import admin
from cadasta_plugins.models.plugin import Plugin
from cadasta_plugins.models.release import Release


# Register your models here.
class PluginAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('version', 'date', 'get_plugin_name')

    def get_plugin_name(self, obj):
        return obj.plugin.name

admin.site.register(Plugin, PluginAdmin)
admin.site.register(Release, ReleaseAdmin)
