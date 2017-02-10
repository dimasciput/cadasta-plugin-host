from django.contrib import admin
from .models.plugins import Plugin


# Register your models here.
class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'date')
    search_fields = ['name', 'version']


admin.site.register(Plugin, PluginAdmin)
