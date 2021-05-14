from django.contrib import admin

# Register your models here.
from .models import *


class DictionariesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'note', 'date_created', 'hierarchy')
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


admin.site.register(ModelsHierarchy, ModelsHierarchyModelAdmin)
admin.site.register(Locations, LocationsModelAdmin)
admin.site.register(Productions, DictionariesAdmin)
admin.site.register(Workshops, DictionariesAdmin)
admin.site.register(Compartments, DictionariesAdmin)

# class DictAdmin(admin.ModelAdmin):
#     list_display = ('id')
# list_display_links = ('id', 'name')
# search_fields = ('id', 'note')


# class SwitchCabinetsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'number', 'location_id', 'Compartments.name')
#
#
# class LocationsAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'production_id', 'workshop_id', 'compartment_id')
#     # list_filter = ('production_id', 'workshop_id', 'compartment_id')


# class SwitchCabinetsAdmin(admin.ModelAdmin):
#     def getProductionsName(self, obj):
#         res = obj.location_id.production_id.name_productions
#         return res
#
#     def getWorkshopsName(self, obj):
#         res = obj.location_id.workshop_id.name_workshops
#         return res
#
#     def getCompartmentsName(self, obj):
#         res = obj.location_id.compartment_id.name_compartments
#         return res
#
#     getProductionsName.short_description = 'Производство'
#     getWorkshopsName.short_description = 'Цех'
#     getCompartmentsName.short_description = 'Участок'
#
#     list_display = ('pk', 'name_switch_cabinets', 'getProductionsName', 'getWorkshopsName', 'getCompartmentsName')
#     # list_filter = ('production_id', 'workshop_id', 'compartment_id')


# admin.site.register(Locations, LocationsAdmin)
# admin.site.register(SwitchCabinets, SwitchCabinetsAdmin)
# admin.site.register(Stations)
# admin.site.register(ControllerFamilies)
# admin.site.register(Compartments)
# admin.site.register(Productions)
# admin.site.register(Workshops)
