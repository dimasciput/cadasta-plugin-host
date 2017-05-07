from django.contrib import admin
from plugins.models.plugin import Plugin
from plugins.models.release import Release
from plugins.models.tag import Tag


# Register your models here.
class PluginAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('version', 'date', 'plugin_name')

    def plugin_name(self, obj):
        return obj.plugin.name


admin.site.register(Plugin, PluginAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Tag)
