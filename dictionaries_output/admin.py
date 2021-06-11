from django.contrib import admin
from .models import *


class DictionariesAdmin(admin.ModelAdmin):
    def get_hierarchy_note(self, obj):
        hierarchy_note = obj.hierarchy.note
        return hierarchy_note

    get_hierarchy_note.short_description = 'Иерархия'
    list_display = ('pk', 'name', 'note', 'date_created', 'get_hierarchy_note')
    list_display_links = ('pk', 'name')
    search_fields = ('pk', 'name')


class WorkshopsAdmin(admin.ModelAdmin):
    def get_hierarchy_note(self, obj):
        hierarchy_note = obj.hierarchy.note
        return hierarchy_note

    get_hierarchy_note.short_description = 'Иерархия'
    list_display = ('pk', 'name', 'note', 'date_created', 'get_hierarchy_note', 'production_id')
    list_display_links = ('pk', 'name')
    search_fields = ('pk', 'name')


class CompartmentsAdmin(admin.ModelAdmin):
    def get_hierarchy_note(self, obj):
        hierarchy_note = obj.hierarchy.note
        return hierarchy_note

    get_hierarchy_note.short_description = 'Иерархия'
    list_display = ('pk', 'name', 'note', 'date_created', 'get_hierarchy_note', 'production_id', 'workshop_id')
    list_display_links = ('pk', 'name')
    search_fields = ('pk', 'name')


class LocationsModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'production_id', 'workshop_id', 'compartment_id', 'note', 'date_created')
    list_display_links = ('pk', 'production_id', 'workshop_id', 'compartment_id')
    search_fields = ('pk', 'production_id', 'workshop_id', 'compartment_id')


class ModelsHierarchyModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'hierarchy_number', 'note', 'date_created')
    list_display_links = ('pk', 'hierarchy_number')
    search_fields = ('pk', 'hierarchy_number')


class StationsAdmin(admin.ModelAdmin):
    def get_hierarchy_note(self, obj):
        hierarchy_note = obj.hierarchy.note
        return hierarchy_note

    get_hierarchy_note.short_description = 'Иерархия'
    list_display = ('pk', 'name', 'note', 'date_created', 'get_hierarchy_note', 'ip_adress', 'production_id',
                    'workshop_id', 'compartment_id')
    list_display_links = ('pk', 'name')
    search_fields = ('pk', 'name')


admin.site.register(ModelsHierarchy, ModelsHierarchyModelAdmin)
admin.site.register(Locations, LocationsModelAdmin)
admin.site.register(Productions, DictionariesAdmin)
admin.site.register(Workshops, WorkshopsAdmin)
admin.site.register(Compartments, CompartmentsAdmin)
admin.site.register(Stations, StationsAdmin)
admin.site.register(SwitchCabinets)
